from re import compile
from aiohttp import ClientSession
from discord import Message, TextChannel
from discord.ext import commands
from discord.ext.commands import Context 
from Cogs.Utils.custom_bot import CustomBot
from Cogs.Utils.custom_embed import CustomEmbed


class Okay_Google(object):

    def __init__(self, bot:CustomBot):
        self.bot = bot
        self.session = ClientSession(loop=bot.loop)
        self.matcher = compile(r'(ok(ay)?|(al)?right) google,? (.*)')


    def __unload(self):
        self.session.close()


    async def __before_invoke(self, ctx:Context):
        await ctx.trigger_typing()


    async def run_google_search(self, query:str, channel:TextChannel) -> CustomEmbed:
        '''
        This is the actual command that gets the data back from Google
        It's provided as a seperate function so as to be used by both the command
        and by the on_message invoke
        '''

        # See if it's a NSFW channel
        safe = 'off' if channel.is_nsfw() else 'high'

        # Generate the params
        params = {
            'cx': self.bot.config['API Keys']['GoogleCustomSearchID'],
            'q': query,
            'key': self.bot.config['API Keys']['GoogleCustomSearchKey'],
            'num': 1,
            'safe': safe
        }

        # Send the request
        url = 'https://www.googleapis.com/customsearch/v1'
        async with self.session.get(url, params=params) as r:
            output = await r.json()

        # Return 
        data = output['items'][0]
        with CustomEmbed() as e:
            e.set_author(name=data.get('title'), url=data.get('link'))
            if data.get('metatags'):

                # Get a description
                meta_list = data.get('metatags')
                isset = False

                # Metatag description is better than the HTML snippet
                # Iterate through the metatags set
                for meta in meta_list:
                    if isset == False:

                        # If it ends with "description, set it as the description"
                        for k, v in meta.items():
                            if k.lower().endswith('description'):
                                e.description = v
                                isset = True
                                break

            elif data.get('snippet'):
                e.description = data.get('snippet').replace('\n', ' ')[:200] + '...'

            try:
                e.set_thumbnail(url=data['pagemap']['cse_thumbnail'][0]['src'])
            except KeyError:
                pass
        return e


    @commands.command()
    async def google(self, ctx:Context, *, query:str):
        '''
        Searches a given phrase by Google
        '''

        e = await self.run_google_search(query, ctx.channel)
        await ctx.send(embed=e)


    async def on_message(self, message:Message):
        '''
        Used to trigger the invocation of 'okay google'
        '''

        # Check that it's enabled
        async with self.bot.database() as db:
            try:
                x = await db('SELECT okay_google_enabled FROM guild_config WHERE guild_id=$1', message.guild.id)
            except Exception as e:
                return
        if not x[0]['okay_google_enabled']:
            return

        content = message.content
        matches = self.matcher.match(content)
        if matches:
            await message.channel.trigger_typing()
            e = await self.run_google_search(matches.group(4), message.channel)
            e.set_footer(text='To disable this, run the `disablegoogle` command')
            await message.channel.send(embed=e)


def setup(bot:CustomBot):
    x = Okay_Google(bot)
    bot.add_cog(x)
