import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help

import asyncio
import os


default_settings = {"mode": "DM", "rules": None, "kick_message": "Too bad", "on": False,
                    "role_before": None, "role_after": None,
                    "welcome_message": "Enjoy your stay", "logchannel": None,
                    "timeout_message": "You took too long to respond. You may rejoin"}


class Bouncer:
    """Greets joining members"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/bouncer/settings.json")

    @checks.admin()
    @commands.group(pass_context=True)
    async def bouncerset(self, ctx):
        """Settings for bouncer"""
        server = ctx.message.server
        if server.id not in self.settings:
            self.settings[server.id] = default_settings
            dataIO.save_json('data/bouncer/settings.json', self.settings)
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            return

    @bouncerset.command(pass_context=True, name="toggle")
    async def bouncerset_toggle(self, ctx, on_off: bool):
        """Toggles bouncin'"""
        server = ctx.message.server
        self.settings[server.id]["on"] = on_off
        if on_off:
            await self.bot.say("Bouncin' enabled")
        else:
            await self.bot.say("Will not bounce (???)")
        dataIO.save_json('data/bouncer/settings.json', self.settings)

    @bouncerset.command(pass_context=True, name="mode")
    async def bouncerset_mode(self, ctx, DM_channel):
        """Toggles mode. DM will DM the user, channel will create a
        private channel session with the user and delete it afterds"""
        valid_options = ["dm", "channel"]
        if DM_channel.lower() not in valid_options:
            await send_cmd_help(ctx)
            return
        server = ctx.message.server
        self.settings[server.id]["mode"] = DM_channel.lower()
        # TODO test.func
        if DM_channel.lower() == "dm":
            await self.bot.say("Will DM new users")
        else:
            await self.bot.say("Will open channel with new users")
        dataIO.save_json('data/bouncer/settings.json', self.settings)

    @bouncerset.command(pass_context=True, name="rules")
    async def bouncerset_rules(self, ctx, *, message: str):
        """This message will be shown to new people joining the server, with
        reaction emojis to either agree or disagree.
        {0} is member
        {1} is server
        """
        server = ctx.message.server
        self.settings[server.id]["rules"] = message
        await self.bot.say("Rules set to: {0}".format(message))
        dataIO.save_json('data/bouncer/settings.json', self.settings)

    @bouncerset.command(pass_context=True, name="welcomemessage")
    async def bouncerset_welcomemessage(self, ctx, *, message: str):
        """This message will be shown to people which accept the rules
        """
        server = ctx.message.server
        self.settings[server.id]["welcome_message"] = message
        await self.bot.say("Welcome message set to: {0}".format(message))
        dataIO.save_json('data/bouncer/settings.json', self.settings)

    @bouncerset.command(pass_context=True, name="kickmessage")
    async def bouncerset_kickmessage(self, ctx, *, message: str):
        """This message will be delivered to people who disagree to rules"""
        server = ctx.message.server
        self.settings[server.id]["kick_message"] = message
        await self.bot.say("Kick message set to: {0}".format(message))
        dataIO.save_json('data/bouncer/settings.json', self.settings)

    @bouncerset.command(pass_context=True, name="timeoutmessage")
    async def bouncerset_timeoutmessage(self, ctx, *, message: str):
        """This message will be delivered to people who don't react either way for 5 minutes

        Should probably include a tutorial on how to use it, and
        maybe invite link back to the server.
        """
        server = ctx.message.server
        self.settings[server.id]["timeout_message"] = message
        await self.bot.say("Timeout message set to: {0}".format(message))
        dataIO.save_json('data/bouncer/settings.json', self.settings)

    @bouncerset.command(pass_context=True, name="logchannel")
    async def bouncerset_logchannel(self, ctx, channel: discord.Channel=None):
        """A channel to send messages to whenever some error occurs, user
        agress/disagress with the rules or times out
        This is to ensure bot doesn't lock anybody out.
        """
        server = ctx.message.server
        if not server.me.permissions_in(channel).send_messages:
            await self.bot.say("No permissions to speak in that channel")
            return
        self.settings[server.id]["logchannel"] = channel.id
        dataIO.save_json('data/bouncer/settings.json', self.settings)
        await self.bot.send_message(channel, "I will now send bouncer logs here.")

    @bouncerset.command(pass_context=True, name="roles")
    async def bouncerset_roles(self, ctx, before_after: str, role: discord.Role=None):
        """For first parameter use before or after. For roles with space with them,
        use \"double quotes\"

        Before: role assigned to users when they join the server but don't accept
        the rules yet, will be stripped after accepting the rules. Can be left empty.

        After: Role assigned after accepting the rules
        """
        server = ctx.message.server
        valid_options = ["before", "after"]
        selection = before_after.lower()
        if selection not in valid_options:
            await send_cmd_help(ctx)
            return
        if selection == "before":
            await self.bot.say("Role assigned at join will be: {}".format(role))
            self.settings[server.id]["role_before"] = role.id
        elif role is not None:
            await self.bot.say("Role assigned after accepting rules will be: {}".format(role))
            self.settings[server.id]["role_after"] = role.id
        else:
            self.bot.say("After role can't be empty")
            return
        dataIO.save_json('data/bouncer/settings.json', self.settings)

    async def bounce(self, target, message, user):
        try:
            msg = await self.bot.send_message(target, message)
            await asyncio.sleep(5)
            await self.bot.add_reaction(msg, "✅")
            await self.bot.add_reaction(msg, "❌")
            result = await self.bot.wait_for_reaction(['✅', '❌'], message=msg, user=user, timeout=300)
            if result is None:
                return None
            if result.reaction.emoji == "✅":
                return True
            elif result.reaction.emoji == "❌":
                return False
        except Exception as e:
            print("[Bouncer] Tried to send message to {} but failed. "
                  "Probably DMs diasbled. Error: {}".format(target, e))

    async def writelog(self, server, message):
        log_channel = self.settings[server.id]["logchannel"]
        if not log_channel:
            return
        channel = server.get_channel(log_channel)
        try:
            await self.bot.send_message(channel, message)
        except:
            print("Even writing logs failed. God help you.")

    async def on_member_join(self, member):
        server = member.server
        channel = server.default_channel
        if member.bot:  # BotRights
            return
        if server.id not in self.settings:
            self.settings[server.id] = default_settings
            dataIO.save_json('data/bouncer/settings.json', self.settings)
        settings = self.settings[server.id]
        if not settings["on"]:
            return
        perms = channel.permissions_for(server.me)
        manage_channels = perms.manage_channels
        add_reactions = perms.add_reactions
        kick_members = perms.kick_members
        manage_roles = perms.manage_roles
        read_messages = perms.read_messages
        send_messages = perms.send_messages
        can_proceed = manage_channels and add_reactions and kick_members and manage_roles and read_messages and send_messages
        if not can_proceed:
            error = ("Permission missing. Neccesary permissions: Manage channels, "
                     "add reactions, kick members, manage roles, read messages, send messages")
            print(error)
            await self.writelog(server, error)
            return
        mode = settings["mode"]
        role_before = discord.utils.get(
            server.roles, id=settings["role_before"]) if settings["role_before"] else None
        role_after = discord.utils.get(server.roles, id=settings["role_after"])
        rules = settings["rules"]
        welcome_message = settings["welcome_message"]
        kick_message = settings["kick_message"]
        timeout_message = settings["timeout_message"]
        if not role_after:
            error = "After-role is not set, aborting"
            print(error)
            await self.writelog(server, error)
            return
        if not kick_message or not welcome_message:
            error = "Missing message in settings, aborting"
            print(error)
            await self.writelog(server, error)
            return
        if role_before:
            await self.bot.add_roles(member, role_before)
        try:
            if mode == "dm":
                result = await self.bounce(member, rules.format(member, server), member)
                if result:
                    await self.bot.send_message(member, welcome_message)
                    if role_before:
                        await self.bot.remove_roles(member, role_before)
                    await self.bot.add_roles(member, role_after)
                    await self.writelog(server, "{0.name} has accepted the rules".format(member))
                if not result and result is not None:
                    await self.bot.send_message(member, kick_message)
                    await self.bot.kick(member)
                    await self.writelog(server, "{0.name} has denied the rules and been kicked".format(member))
                elif result is None:
                    await self.bot.send_message(member, timeout_message)
                    await self.bot.kick(member)
                    await self.writelog(server, "{0.name} has timed out".format(member))
            else:
                channel_name = "Welcome_" + member.id
                everyone_perms = discord.PermissionOverwrite(
                    read_messages=False)
                user_perms = discord.PermissionOverwrite(
                    read_messages=True, add_reactions=False, read_message_history=True)
                bot_perms = discord.PermissionOverwrite(
                    read_messages=True, add_reaction=True, manage_channels=True)
                everyone = discord.ChannelPermissions(
                    target=server.default_role, overwrite=everyone_perms)
                user = discord.ChannelPermissions(
                    target=member, overwrite=user_perms)
                bot = discord.ChannelPermissions(
                    target=server.me, overwrite=bot_perms)
                channel = await self.bot.create_channel(server, channel_name, everyone, user, bot)
                result = await self.bounce(channel, rules.format(member, server), member)
                if result:
                    await self.bot.send_message(channel, welcome_message)
                    if role_before:
                        await self.bot.remove_roles(member, role_before)
                    await self.bot.add_roles(member, role_after)
                    await self.writelog(server, "{0.name} has accepted the rules".format(member))
                    await asyncio.sleep(180)
                    await self.bot.delete_channel(channel)
                if not result and result is not None:
                    await self.bot.delete_channel(channel)
                    await self.bot.send_message(member, kick_message)
                    await self.bot.kick(member)
                    await self.writelog(server, "{0.name} has denied the rules and been kicked".format(member))
                elif result is None:
                    await self.bot.delete_channel(channel)
                    await self.bot.send_message(member, timeout_message)
                    await self.bot.kick(member)
                    await self.writelog(server, "{0.name} has timed out".format(member))
        except discord.errors.Forbidden:
            print("Missing neccesary permisions. Ugh..")
            await self.writelog(server, "Missing some permission, member might be stuck")
        except Exception as e:
            print(
                "[Bouncer]. Error: {}".format(e))
            await self.writelog(server, "Unknown exception occured: {}. User is probably stuck,".format(e))


def check_folders():
    if not os.path.exists("data/bouncer"):
        print("Creating data/bouncer")
        os.makedirs("data/bouncer")


def check_files():
    f = "data/bouncer/settings.json"
    if not dataIO.is_valid_json(f):
        print("Creating empty bouncer/settings.json...")
        dataIO.save_json(f, {})


def setup(bot):
    check_folders()
    check_files()
    n = Bouncer(bot)
    bot.add_cog(n)
