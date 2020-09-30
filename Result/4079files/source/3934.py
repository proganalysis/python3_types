from aiohttp import ClientSession
from discord.ext import commands
from discord.ext.commands import Context
from Cogs.Utils.custom_bot import CustomBot
from Cogs.Utils.bibleify import Bible


class Bible_Commands(object):

    def __init__(self, bot:CustomBot):
        self.bot = bot
        self.session = ClientSession(loop=bot.loop)


    def __unload(self):
        self.session.close()


    async def __before_invoke(self, ctx:Context):
        await ctx.trigger_typing()


    @commands.command()
    async def bible(self, ctx:Context, *, passage:str):
        '''
        Gives you a passage, or set of passages, from the Christian Bible
        '''

        ENDPOINT = 'https://getbible.net/json?scrip='

        # Run the request to try and get it
        async with self.session.get(ENDPOINT + passage) as r:
            text = await r.read()

        # Try and transform it into data
        try:
            data = eval(text[1:-2])  # Semi-eqiv to r.json(), but I just need to trim some characters
        except NameError:
            await ctx.send('That request was malformed and could not be found on the server.')
            return

        # Now I need to bibleify it
        bible_data = Bible(data)
        embed = bible_data.to_embed()
        await ctx.send(embed=embed)


def setup(bot:CustomBot):
    x = Bible_Commands(bot)
    bot.add_cog(x)
