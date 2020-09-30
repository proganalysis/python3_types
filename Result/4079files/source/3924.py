import discord
from discord.ext import commands


class GuildConverter(commands.IDConverter):
    """Converts to a :class:`Guild`.
    All lookups are done via global guild cache.
    The lookup strategy is as follows (in order):
    1. Lookup by ID
    2. Lookup by name
    """
    async def convert(self, ctx: commands.Context, argument: str):
        bot = ctx.bot
        match = self._get_id_match(argument)

        if match is None:
            result = discord.utils.get(bot.guilds, name=argument)
        else:
            guild_id = int(match.group(1))
            result = bot.get_guild(guild_id)

        if not isinstance(result, discord.Guild):
            raise commands.BadArgument(f'Guild "{argument}" not found.')

        return result


class UserInfoConverter(commands.IDConverter):
    """Converts to a :class:`User`.
    lookups are done via both local and global caches
    the lookup stragegy is as follows (in order):
    1. Lookup by local `commands.converter.UserConverter`
    2. Lookup in global search (bot accounts only)
    """
    async def convert(self, ctx: commands.Context, argument: str):
        bot = ctx.bot
        match = self._get_id_match(argument)

        try:
            instance = commands.converter.UserConverter()
            result = await instance.convert(ctx, argument)
        except commands.BadArgument:
            if match and bot.user.bot:
                try:
                    user_id = int(match.group(1))
                    result = await bot.get_user_info(user_id)
                except discord.NotFound:
                    result = None
            else:
                result = None

        if not isinstance(result, discord.User):
            raise commands.BadArgument(f'User "{argument}" not found.')

        return result


class UnspecifiedConverter(commands.IDConverter):
    """Converts to any of the following:
    :class:`Guild`, :class:`TextChannel`, :class:`VoiceChannel`,
    :class:`Role`, :class:`Member`, :class:`User`
    all lookups are done via both local and global caches
    the lookup strtegy is as follows (in order):
    Roles and Members are guild specific
    1. Guild
    2. Role
    3. CategoryChannel
    4. TextChannel
    5. VoiceChannel
    6. Member
    7. User
    8. Emoji
    9. Colour
    10. Invite
    """
    async def convert(self, ctx: commands.Context, argument: str):
        converters = [
            GuildConverter,
            commands.converter.RoleConverter,
            commands.converter.CategoryChannelConverter,
            commands.converter.TextChannelConverter,
            commands.converter.VoiceChannelConverter,
            commands.converter.MemberConverter,
            UserInfoConverter,
            commands.converter.EmojiConverter,
            commands.converter.ColourConverter,
            commands.converter.InviteConverter,
        ]
        result = None

        for converter in converters:
            try:
                instance = converter()
                if isinstance(instance, commands.converter.MemberConverter) and isinstance(ctx.channel, discord.DMChannel):
                    continue
                result = await instance.convert(ctx, argument)
                break
            except (commands.BadArgument, commands.NoPrivateMessage):
                continue

        if result is None:
            raise commands.BadArgument(f'Item "{argument}" not found.')

        return result
