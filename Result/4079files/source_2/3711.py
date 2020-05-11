# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2017 - 2018 FrostLuma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import inspect

import discord
from discord.ext import commands
from discord.ext.commands.view import quoted_word

from .context import Context
from .converter import MultiConverter
from .errors import CommandError, BadArgument, BotMissingPermissions, MissingRequiredArgument, MissingPermissions


check = commands.check
guild_only = commands.guild_only
is_nsfw = commands.is_nsfw
is_owner = commands.is_owner


def _get_words(view):
    while not view.eof:
        view.skip_ws()

        yield quoted_word(view)


class RecalledArgument:
    """
    Converters may return parts of the given argument(s) to be re-used on the next parameter the command has.

    This allows for having multi word arguments in the middle of commands: command <multi word> <rest>
    As well as having optional arguments in between required ones: command <argument=default> <required>
    """

    def __init__(self, argument: str):
        self.argument = argument


class Command(commands.Command):
    """
    Extension of the default command to extend functionality.

    Parameters
    ----------
    typing : bool
        Whether the bot should type in the current channel while executing this command. Defaults to False.
    """

    def __init__(self, *, typing=False, **kwargs):
        super().__init__(**kwargs)

        self.typing = typing

    async def do_conversion(self, ctx, converter, argument):
        if converter is bool:
            return commands.core._convert_to_bool(argument)

        if converter.__module__.startswith('discord.') and not converter.__module__.endswith('converter'):
            converter = getattr(commands.converter, converter.__name__ + 'Converter')

        if inspect.isclass(converter):
            if issubclass(converter, MultiConverter):
                ret = []
                word = ''

                instance = converter()

                for word in _get_words(argument):
                    try:
                        result = await instance.convert(ctx, word)
                    except (BadArgument, ValueError, TypeError):
                        break
                    else:
                        word = ''
                        ret.append(result)

                # check if no things could be converted and this param is required
                # this will raise a MissingRequiredArgument if needed in the transform method
                if argument.required and not ret:
                    return RecalledArgument(word)

                return ret, RecalledArgument(word)

            if issubclass(converter, commands.Converter):
                instance = converter()
                ret = await instance.convert(ctx, argument)
                return ret

            method = getattr(converter, 'convert', None)

            if method is not None and inspect.ismethod(method):
                ret = await method(ctx, argument)
                return ret

        elif isinstance(converter, commands.Converter):
            ret = await converter.convert(ctx, argument)
            return ret

        return converter(argument)

    async def transform(self, ctx: Context, param):
        required = param.default is param.empty
        converter = self._get_converter(param)
        consume_rest_is_special = param.kind == param.KEYWORD_ONLY and not self.rest_is_raw

        view = ctx.view
        view.skip_ws()

        if view.eof:
            if param.kind == param.VAR_POSITIONAL:
                raise RuntimeError()  # break the loop
            if required:
                raise MissingRequiredArgument(param)
            return param.default

        if inspect.isclass(converter) and issubclass(converter, MultiConverter):
            argument = view
            argument.required = required  # we don't want to change the method signature but need this value
        elif consume_rest_is_special:
            argument = view.read_rest().strip()
        else:
            argument = quoted_word(view)

        try:
            result = await self.do_conversion(ctx, converter, argument)
        except CommandError as e:
            raise e
        except Exception as e:
            try:
                name = converter.__name__
            except AttributeError:
                name = converter.__class__.__name__

            raise BadArgument(f'Converting to "{name}" failed for parameter "{param.name}".') from e

        if isinstance(result, RecalledArgument):
            if required:
                raise MissingRequiredArgument(param)

            view.index -= len(result.argument) if ' ' not in result.argument else len(result.argument) + 2

            result = param.default

        elif isinstance(result, tuple) and isinstance(result[-1], RecalledArgument):
            *result, recalled = result
            view.index -= len(recalled.argument) if ' ' not in recalled.argument else len(recalled.argument) + 2

            if len(result) == 1:
                result = result[0]

        return result

    async def _parse_arguments(self, ctx: Context):
        ctx.args = args = [ctx] if self.instance is None else [self.instance, ctx]
        ctx.kwargs = kwargs = {}

        view = ctx.view
        iterator = iter(self.params.items())

        if self.instance is not None:
            # we have 'self' as the first parameter so just advance
            # the iterator and resume parsing
            try:
                next(iterator)
            except StopIteration:
                raise discord.ClientException(f'Callback for {self.name} command is missing "self" parameter.')

        # next we have the 'ctx' as the next parameter
        try:
            next(iterator)
        except StopIteration:
            raise discord.ClientException(f'Callback for {self.name} command is missing "ctx" parameter.')

        for name, param in iterator:
            if param.kind == param.POSITIONAL_OR_KEYWORD:
                transformed = await self.transform(ctx, param)
                args.append(transformed)

            elif param.kind == param.KEYWORD_ONLY:
                # kwarg only param denotes "consume rest" semantics
                if self.rest_is_raw:
                    converter = self._get_converter(param)
                    argument = view.read_rest()
                    kwargs[name] = await self.do_conversion(ctx, converter, argument)
                    break

                kwargs[name] = await self.transform(ctx, param)

            elif param.kind == param.VAR_POSITIONAL:
                while not view.eof:
                    try:
                        transformed = await self.transform(ctx, param)
                        args.append(transformed)
                    except RuntimeError:
                        break

        if not self.ignore_extra:
            if not view.eof:
                raise commands.TooManyArguments(f'Too many arguments passed to {self.qualified_name}')

    async def invoke(self, ctx):
        # this is basically copied from the superclass
        # the actual_invoke func is there to not type during preparation (verifying checks etc)
        await self.prepare(ctx)

        async def actual_invoke():
            ctx.invoked_subcommand = None
            injected = commands.core.hooked_wrapped_callback(self, ctx, self.callback)
            await injected(*ctx.args, **ctx.kwargs)

        if self.typing:
            async with ctx.typing():
                return await actual_invoke()
        await actual_invoke()


class GroupMixin(commands.GroupMixin):
    # shortcut decorators to add commands and groups to the internal commands list
    # these are just copied from the superclass to use the new Command class
    def command(self, *args, **kwargs):
        def decorator(func):
            cmd = command(*args, **kwargs)(func)
            self.add_command(cmd)
            return cmd

        return decorator

    def group(self, *args, **kwargs):
        def decorator(func):
            cmd = group(*args, **kwargs)(func)
            self.add_command(cmd)
            return cmd

        return decorator


class Group(GroupMixin, commands.Group, Command):
    pass


def command(name: str=None, cls=Command, **attrs):
    return commands.command(name, cls, **attrs)


def group(name: str=None, invoke_without_command: bool=True, **attrs):
    return command(name, cls=Group, invoke_without_command=invoke_without_command, **attrs)


def schedule(interval,  wait_until_ready=True, run_once=False):
    """
    Schedule a method to be called later, on a specified interval.

    .. note:: The interval is also the initial sleep, the method will not get called immediately after startup

    Parameters
    ----------
    interval : int
        Seconds to wait between calling the method
    wait_until_ready : bool
        Whether to wait until the bot has logged in before running for the first time, defaults to True
    run_once
        Whether this method should only be called once or on the interval
    """

    def decorator(func):
        func.__schedule = {'interval': interval, 'wait_until_ready': wait_until_ready, 'run_once': run_once}
        return func

    return decorator


def when_ready(func):
    """
    Schedule a method to be called when the bot is ready or whenever the cog loads.
    This will be called every time the ready event is dispatched, not just the first time.
    """

    func.__schedule = {'on_ready': True}
    return func


def _has_permissions(ctx, target, **perms):
    """
    Checks whether the target has all given permissions in the current channel.

    The permissions must match the attribute names of cls discord.Permissions.
    https://discordpy.readthedocs.io/en/rewrite/api.html#permissions

    .. note :: To make commands visible in help commands the check will return True if the bot is being checked,
               even if the check should fail.

    Parameters
    ----------
    ctx : Context
        The current context to look up permissions in
    target : Union[discord.Member, discord.User]
        The user to check the permissions of
    perms : dict
        permission: required value pairs of permissions.

    Returns
    -------
    bool
        Whether the user has all the permissions

    Raises
    ------
    InsufficientPermissions
        If the target is the bot user and does not have all required permissions
    MissingPermissions
        If any other user does not have all required permissions
    """

    if target == ctx.bot.user and ctx.invoked_with == 'help':
        return True

    target_perms = ctx.channel.permissions_for(target)

    # administrator means this user has all the other permissions
    if target_perms.administrator:
        return True

    missing = [perm for perm in perms if not getattr(target_perms, perm, False)]

    if not missing:
        return True

    # if the target is the bot raise a different error to make catching it separately easier
    if target.id == ctx.me.id:
        raise BotMissingPermissions(missing)
    raise MissingPermissions(*missing)


def has_permissions(**perms):
    """Decorator to add a permission check to a command. This checks the bots and the users permissions."""
    def predicate(ctx: Context) -> bool:
        return _has_permissions(ctx, ctx.author, **perms) and _has_permissions(ctx, ctx.me, **perms)
    return check(predicate)


def bot_has_permissions(**perms):
    """Decorator to add a permission check to a command. This checks the bots permissions."""
    def predicate(ctx: Context) -> bool:
        return _has_permissions(ctx, ctx.me, **perms)
    return check(predicate)


def user_has_permissions(**perms):
    """Decorator to add a permission check to a command. This checks the only users (authors) permissions."""
    def predicate(ctx: Context) -> bool:
        return _has_permissions(ctx, ctx.author, **perms)
    return check(predicate)
