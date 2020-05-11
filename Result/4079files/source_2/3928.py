import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help

import asyncio
import os


class NameChange:
    """Name change notifications"""

    def __init__(self, bot):
        self.bot = bot
        self.cooldown = {}
        self.settings = dataIO.load_json("data/namechange/settings.json")

    @checks.mod_or_permissions(manage_messages=True)
    @commands.group(pass_context=True)
    async def namechangeset(self, ctx):
        """Settings for name change notifications"""
        server = ctx.message.server
        if server.id not in self.settings:
            self.settings[server.id] = {
                "channel": None, "cooldown": 600, "on": False}
            dataIO.save_json('data/namechange/settings.json', self.settings)
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            return

    @namechangeset.command(pass_context=True, name="toggle")
    async def namechangeset_toggle(self, ctx, on_off: bool):
        """Toggles sending name change notifications"""
        server = ctx.message.server
        self.settings[server.id]["on"] = on_off
        channel = server.get_channel(self.settings[server.id]["channel"])
        output = "Current channel: {0.mention}".format(
            channel) if channel else "No notification channel is set, though."
        if on_off:
            await self.bot.say(
                "Name change notifications are enabled. {0}".format(output))
        else:
            await self.bot.say("Will not send name change notifications")
        dataIO.save_json('data/namechange/settings.json', self.settings)

    @namechangeset.command(pass_context=True, name="channel")
    async def namechangeset_channel(self, ctx, channel: discord.Channel):
        """Sets channel for name change notifications"""
        server = ctx.message.server
        if not server.get_member(self.bot.user.id).permissions_in(channel).send_messages:
            await self.bot.say("Cant send messages to that channel")
            return
        await self.bot.send_message(channel, "Will send name change notifications"
                                             " to {0.mention}".format(channel))
        self.settings[server.id]["channel"] = channel.id
        dataIO.save_json('data/namechange/settings.json', self.settings)

    @namechangeset.command(pass_context=True, name="cooldown")
    async def namechangeset_cooldown(self, ctx, seconds: int):
        """Sets the cooldown between sending new message about name change"""
        server = ctx.message.server
        await self.bot.say("Cooldown is now {0} seconds".format(seconds))
        self.settings[server.id]["cooldown"] = seconds
        dataIO.save_json('data/namechange/settings.json', self.settings)

    async def on_member_update(self, before, after):
        if before.server.id not in self.settings:
            return
        if not self.settings[before.server.id]["on"]:
            return
        if before.nick != after.nick:
            nickname = before.nick if before.nick else before.name
            server = before.server
            output = "{0} changed their name to {1.mention}".format(
                nickname, after)
            color = discord.Colour.dark_green()
            data = discord.Embed(description=None, colour=color)
            data.add_field(name="Name changed", value=output)
            data.set_author(name=after.name)
            if before.id in self.cooldown:
                message = self.cooldown[before.id]
                await self.bot.edit_message(message, embed=data)
            else:
                if not self.settings[server.id]["channel"]:
                    return
                channel = server.get_channel(
                    self.settings[server.id]["channel"])
                try:
                    message = await self.bot.send_message(channel, embed=data)
                    self.cooldown[before.id] = message
                    await self.purger_task(before)
                except discord.HTTPException:
                    await self.bot.say("Need permission to embed links")




    async def purger_task(self, member):
        server = member.server
        cooldown = self.settings[server.id]["cooldown"]
        await asyncio.sleep(cooldown)
        self.cooldown.pop(member.id)


def check_folders():
    if not os.path.exists("data/namechange"):
        print("Creating data/namechange")
        os.makedirs("data/namechange")


def check_files():
    f = "data/namechange/settings.json"
    if not dataIO.is_valid_json(f):
        print("Creating empty namechange/settings.json...")
        dataIO.save_json(f, {})


def setup(bot):
    check_folders()
    check_files()
    n = NameChange(bot)
    bot.add_cog(n)
