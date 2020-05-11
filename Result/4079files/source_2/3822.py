from discord import VoiceChannel, PCMVolumeTransformer, FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands import Context
from Cogs.Utils.custom_bot import CustomBot
from Cogs.Utils.youtube_downloader import YTDL_Source


class Music_Commands(object):
    def __init__(self, bot:CustomBot):
        self.bot = bot
        self.queue = {}  # GuildID: List[str]

    @commands.command()
    async def join(self, ctx:Context, *, channel:VoiceChannel):
        '''
        Joins a voice channel
        '''

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        
        await channel.connect()


    @commands.command()
    async def play(self, ctx:Context, *, url:str):
        '''
        Streams from a URL (almost anything youtube_dl supports)
        '''

        # Works out if it's connected to a VC
        if ctx.voice_client is None:
            if ctx.author.voice.channel:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send('I\'m not currently connected to a voice channel.')
                return

        # If it's playing something, stop it
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        # Create a YTDL object
        player = await YTDL_Source.from_url(url, loop=self.bot.loop)

        # Play it
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        
        # Boop it out to the user
        await ctx.send('Now playing: {}'.format(player.title))
        await ctx.send(player.data)

    @commands.command()
    async def volume(self, ctx:Context, volume:int):
        '''
        Changes the player's volume
        '''

        # Determine if connected
        if ctx.voice_client is None:
            await ctx.send('I\'m not currently connected to a voice channel.')
            return

        # Change the volume of the player
        ctx.voice_client.source.volume = volume if volume <= 100 else 100 if volume >=0 else 0
        await ctx.send('Changed volume to {}%'.format(volume))


    @commands.command()
    async def stop(self, ctx:Context):
        '''
        Stops and disconnects the bot from voice
        '''

        await ctx.voice_client.disconnect()
        await ctx.send('Stopped, disconnected, and cleared queue.')


def setup(bot):
    x = Music_Commands(bot)
    bot.add_cog(x)
