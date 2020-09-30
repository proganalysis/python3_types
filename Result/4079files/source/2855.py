import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from __main__ import send_cmd_help

import asyncio
from random import choice
import os

# From: https://gist.github.com/MetroWind/1401473

CHAR_UP = ['\u030D', '\u030E', '\u0304', '\u0305', '\u033F',
           '\u0311', '\u0306', '\u0310', '\u0352', '\u0357',
           '\u0351', '\u0307', '\u0308', '\u030A', '\u0342',
           '\u0343', '\u0344', '\u034A', '\u034B', '\u034C',
           '\u0303', '\u0302', '\u030C', '\u0350', '\u0300',
           '\u0301', '\u030B', '\u030F', '\u0312', '\u0313',
           '\u0314', '\u033D', '\u0309', '\u0363', '\u0364',
           '\u0365', '\u0366', '\u0367', '\u0368', '\u0369',
           '\u036A', '\u036B', '\u036C', '\u036D', '\u036E',
           '\u036F', '\u033E', '\u035B', '\u0346', '\u031A']

CHAR_MID = ['\u0315', '\u031B', '\u0340', '\u0341', '\u0358',
            '\u0321', '\u0322', '\u0327', '\u0328', '\u0334',
            '\u0335', '\u0336', '\u034F', '\u035C', '\u035D',
            '\u035E', '\u035F', '\u0360', '\u0362', '\u0338',
            '\u0337', '\u0361', '\u0489']

CHAR_DOWN = ['\u0316', '\u0317', '\u0318', '\u0319', '\u031C',
             '\u031D', '\u031E', '\u031F', '\u0320', '\u0324',
             '\u0325', '\u0326', '\u0329', '\u032A', '\u032B',
             '\u032C', '\u032D', '\u032E', '\u032F', '\u0330',
             '\u0331', '\u0332', '\u0333', '\u0339', '\u033A',
             '\u033B', '\u033C', '\u0345', '\u0347', '\u0348',
             '\u0349', '\u034D', '\u034E', '\u0353', '\u0354',
             '\u0355', '\u0356', '\u0359', '\u035A', '\u0323']


default_settings = {"intensity": 1, "up": False, "mid": True, "down": True}


class Zalgo:
    """He comes"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/zalgo/settings.json")

    @commands.group(pass_context=True)
    async def zalgoset(self, ctx):
        """Zalgo settings

        Tied to your own account
        """
        user = ctx.message.author
        if user.id not in self.settings:
            self.settings[user.id] = default_settings
            dataIO.save_json('data/zalgo/settings.json', self.settings)
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            return

    @zalgoset.command(pass_context=True)
    async def intensity(self, ctx, value: int):
        """Values from 1-5. Zalgo intensifies"""
        if not 1 <= value <= 5:
            await send_cmd_help(ctx)
            return
        user = ctx.message.author
        self.settings[user.id]["intensity"] = value
        dataIO.save_json('data/zalgo/settings.json', self.settings)
        settings = self.settings[user.id]
        zalgo_text = self._zalgo_("Zalgo intensifies", settings)
        await self.bot.say(zalgo_text)

    @zalgoset.command(pass_context=True)
    async def up(self, ctx, on_off: bool):
        """Fuck going up?"""
        user = ctx.message.author
        self.settings[user.id]["up"] = on_off
        dataIO.save_json('data/zalgo/settings.json', self.settings)
        if on_off:
            text = "Will now fuck going up"
            output = ""
            for x in text:
                output += x
                output += choice(CHAR_UP)
        else:
            output = "Will not fuck going up"
        await self.bot.say(output)

    @zalgoset.command(pass_context=True)
    async def mid(self, ctx, on_off: bool):
        """Fuck going through the middle?"""
        user = ctx.message.author
        self.settings[user.id]["mid"] = on_off
        dataIO.save_json('data/zalgo/settings.json', self.settings)
        if on_off:
            text = "Will now fuck going through the middle"
            output = ""
            for x in text:
                output += x
                output += choice(CHAR_MID)
        else:
            output = "Will not fuck going through the middle"
        await self.bot.say(output)

    @zalgoset.command(pass_context=True)
    async def down(self, ctx, on_off: bool):
        """Fuck going down?"""
        user = ctx.message.author
        self.settings[user.id]["down"] = on_off
        dataIO.save_json('data/zalgo/settings.json', self.settings)
        if on_off:
            text = "Will now fuck going down"
            output = ""
            for x in text:
                output += x
                output += choice(CHAR_DOWN)
        else:
            output = "Will not fuck going down"
        await self.bot.say(output)

    @zalgoset.command(pass_context=True)
    async def view(self, ctx):
        """Shows your current settings"""
        user = ctx.message.author
        settings = self.settings[user.id]
        zalgo_text = self._zalgo_(
            "these are your current settings: ", settings)
        params = ["intensity", "up", "mid", "down"]
        setlist = "```"
        for p in params:
            setlist += "\n{0} : {1}".format(p.upper(), settings[p])
        setlist += "```"
        output = "{0.mention}, {1} {2}".format(user, zalgo_text, setlist)
        await self.bot.say(output)

    @commands.command(pass_context=True)
    async def zalgo(self, ctx, *, text: str):
        """He comes"""
        user = ctx.message.author
        if user.id in self.settings:
            settings = self.settings[user.id]
        else:
            settings = default_settings
        zalgo_text = self._zalgo_(text, settings)
        try:
            await self.bot.say(zalgo_text)
        except:
            await self.bot.say("This message is too long")

    def _zalgo_(self, text: str, settings):
        output = ""
        intensity = settings["intensity"]
        for x in text:
            output += x
            if settings["up"]:
                for _ in range(intensity):
                    output += choice(CHAR_UP)
            if settings["mid"]:
                for _ in range(intensity):
                    output += choice(CHAR_MID)
            if settings["down"]:
                for _ in range(intensity):
                    output += choice(CHAR_DOWN)
        return output


def check_folders():
    if not os.path.exists("data/zalgo"):
        print("Creating data/zalgo")
        os.makedirs("data/zalgo")


def check_files():
    f = "data/zalgo/settings.json"
    if not dataIO.is_valid_json(f):
        print("Creating empty zalgo/settings.json...")
        dataIO.save_json(f, {})


def setup(bot):
    check_folders()
    check_files()
    n = Zalgo(bot)
    bot.add_cog(n)
