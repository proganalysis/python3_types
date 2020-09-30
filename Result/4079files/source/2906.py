import os
import time
import asyncio
import discord
import subprocess
from .music_type import MusicType
from .music_queue import MusicQueue


class MusicPlayer:
    def __init__(self, cog, voiceClient, server, channel):
        self.queue = MusicQueue()
        self.cog = cog
        self.voiceClient = voiceClient
        self.server = server
        self.channel = channel
        self.player = None
        self.currentSong = None
        self.loop = False

    def makeLocalPlayer(self, fileDir):
        self.player = self.voiceClient.create_ffmpeg_player(fileDir, after=self.afterPlay)

    async def makeYoutubePlayer(self, url):
        self.player = await self.voiceClient.create_ytdl_player(url, after=self.afterPlay)

    def add(self, song):
        self.queue.enqueue(song)

    async def play(self):
        if not self.shouldPlay():
            return
        self.currentSong = self.queue.dequeue()
        if self.currentSong is not None:
            if self.currentSong.type == MusicType.LOCAL or self.currentSong.type == MusicType.TTS:
                self.makeLocalPlayer(self.currentSong.dir)
            elif self.currentSong.type == MusicType.YOUTUBE:
                await self.makeYoutubePlayer(self.currentSong.dir)
            else:
                print("MusicPlayer 재생시 dataType값이 범위 외: {}".format(self.currentType))
                return
            songDesc = "{}을(를) 재생해용".format(self.currentSong.desc())
            await self.cog.bot.send_message(self.channel, songDesc)
            self.player.start()
        else:
            await self.cog.leaveVoice(self.server)

    def stop(self):
        if self.player:
            self.player.stop()
            self.player = None
            if self.currentSong.type == MusicType.TTS:
                os.remove(self.currentSong.dir)
            self.currentSong = None

    async def skip(self):
        self.stop()
        await self.play()

    async def skipIndex(self, ctx, index):
        if 0 <= index <= len(self.queue.list) - 1:
            song = self.queue.list.pop(index)
            await self.cog.bot.send_message(ctx.message.channel, "{}을(를) 재생목록에서 제외했어용".format(song.desc()))
        else:
            await self.cog.bot.send_message(ctx.message.channel, "재생목록의 범위를 넘어섰어용")
            return

    async def printSongList(self, channel):
        if self.queue.empty():
            await self.cog.bot.send_message(channel, "큐가 비어있어용")
        else:
            desc = []
            cnt = 1
            for song in self.queue.list:
                desc.append("`{}`. {}".format(cnt, song.desc()))
                cnt += 1
            await self.cog.bot.send_message(channel, "\n".join(desc)[:2000])

    async def displayCurrentStatus(self, channel):
        if self.player:
            current = int(time.time() - self.player._start)
            if self.currentSong.type == MusicType.LOCAL or self.currentSong.type == MusicType.TTS:
                cmd = 'ffprobe -i \"{}\" -show_entries format=duration -v quiet -of csv="p=0"'.format(self.currentSong.dir)
                result = subprocess.check_output(cmd, shell=True).decode("UTF-8").rstrip()
                total = int(eval(result))
            elif self.currentSong.type == MusicType.YOUTUBE:
                total = self.player.duration
            else:
                return
            percentage = int(current * 10 / total)
            progress = "🎧"
            for i in range(10):
                if i == percentage:
                    progress += "💿"
                else:
                    progress += "▪️"
            title = "{} **{}**".format(MusicType.toEmoji(self.currentSong.type), self.currentSong.name)
            progress += "`[{}/{}]`".format(self.parseTime(current), self.parseTime(total))
            em = discord.Embed(title=title, description=progress, colour=0xDEADBF)
            em.set_footer(text=self.currentSong.user.display_name, icon_url=self.currentSong.user.avatar_url)
            await self.cog.bot.send_message(channel, embed=em)

    def parseTime(self, time):
        timeHour = time // 3600
        timeMin = (time % 3600) // 60
        timeSec = time % 60
        if timeHour > 0:
            return "{}:{:0>2}:{:0>2}".format(timeHour, timeMin, timeSec)
        else:
            return "{:0>2}:{:0>2}".format(timeMin, timeSec)

    def afterPlay(self):
        if self.loop:
            self.queue.enqueue(self.currentSong)
        if self.player.is_done():
            asyncio.run_coroutine_threadsafe(self.skip(), self.cog.loop)

    def shouldPlay(self):
        if not self.player:
            return True
        if not self.player.is_playing():
            return True
        return False
