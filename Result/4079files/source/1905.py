import os
import asyncio
from discord import ChannelType, Forbidden
from discord.ext import commands
from cogs.utils.observable import Observable
from urllib.request import Request, urlopen
from PIL import Image, ImageDraw, ImageFont


class DangerousInvite:
    instance = None

    def __init__(self, bot):
        self.bot = bot
        DangerousInvite.instance = self
        self.games = dict()
        self.errorMsg = "아쉽게도 킥하지 못했서용, 킥할 권한이 없거나 킥할 인간이 서버주인 것 같아용"

        image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data/dinvite"))
        self.baseImage = Image.open("{}/dinvite.jpg".format(image_path))
        self.timeOutImage = Image.open("{}/dinvite_timeout.gif".format(image_path))

        font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data/font"))
        self.fnt = ImageFont.truetype("{}/NanumGothicExtraBold.ttf".format(font_path), 30)

    @commands.command(pass_context=True)
    async def 위험한초대(self, ctx):
        if not self.games.get(ctx.message.server.id) is None:
            await self.bot.say("{}에 의해 게임은 이미 시작되었어용".format(self.games[ctx.message.server.id].initUser.mention))
        else:
            if (ctx.message.channel.type == ChannelType.private):
                return
            try:
                await self.bot.send_message(ctx.message.author, "3글자의 금지단어를 말해주세용")
                await self.bot.add_reaction(ctx.message, "👍")
                newGame = DangerousInviteGame(self.bot, ctx.message.server, ctx.message.author, ctx.message.channel)
                self.games[ctx.message.server.id] = newGame
                self.bot.listenPrivateMsg(newGame)
            except Forbidden:
                await self.bot.say("메시지를 보낼 권한이 없어용")


class DangerousInviteGame(Observable):
    def __init__(self, bot, server, user, channel):
        self.bot = bot
        self.initServer = server
        self.initUser = user
        self.initChannel = channel
        self.started = False
        self.isTimeOut = True
        self.targetWord = None
        self.loop = None
        asyncio.run_coroutine_threadsafe(self.checkStarted(60), self.bot.loop)

    async def checkStarted(self, time):
        await asyncio.sleep(time)
        if not self.started:
            self.endGame()
            await self.bot.send_message(self.initChannel, "{}님 {}초 안에 DM으로 3글자의 메시지를 보내주세용".format(self.initUser.mention, time))

    async def update(self, message):
        if not self.started:
            if len(message.content) is not 3:
                await self.bot.send_message(message.author, "3글자로 입력해주세용")
            else:
                await self.start(message.content)
                await self.bot.send_message(self.initChannel, "{}의 위험한 초대가 시작되었어용!".format(self.initUser.mention))
        else:
            if self.targetWord in message.content:
                await self.gotTargetMessage(message)
                return

    async def start(self, word):
        self.started = True
        self.targetWord = word
        self.bot.dropPrivateMsg(self)
        self.bot.listenPublicMsg(self)
        print("위험한초대가 {}에 의해 {}:{}에서 새로 생성되었어용. 금칙어는 {}(이)에용".format(self.initUser.mention, self.initServer, self.initChannel, self.targetWord))
        asyncio.run_coroutine_threadsafe(self.timeOut(86400), self.bot.loop)

    async def gotTargetMessage(self, message):
        self.isTimeOut = False
        f = open("temp/dinvite_temp.webp", "wb")
        avatarRequest = Request(message.author.avatar_url, headers={"User-Agent": "Mozilla/5.0"})
        f.write(urlopen(avatarRequest).read())
        f.close()

        avatar = Image.open("temp/dinvite_temp.webp").convert("RGB")
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        circleAvatar = avatar.copy()
        circleAvatar.putalpha(mask)

        resultImage = Image.new("RGBA", DangerousInvite.instance.baseImage.size)
        txt = Image.new("RGBA", DangerousInvite.instance.baseImage.size)
        d = ImageDraw.Draw(txt)
        d.text((108, 330), self.targetWord, font=DangerousInvite.instance.fnt, fill=(255, 255, 255, 255))

        resultImage.paste(DangerousInvite.instance.baseImage, (0, 0))
        circleAvatar = circleAvatar.resize((100, 100))
        resultImage.paste(circleAvatar, (128, 99), circleAvatar)
        avatar = avatar.resize((55, 58))
        resultImage.paste(avatar, (49, 320))
        resultImage = Image.alpha_composite(resultImage, txt)
        resultImage.save("temp/dinvite_temp.png", "png")

        with open("temp/dinvite_temp.png", "rb") as f:
            await self.bot.send_file(message.channel, f)

        try:
            await self.bot.kick(message.author)
        except Forbidden:
            await self.bot.send_message(message.channel, DangerousInvite.instance.errorMsg)
        self.endGame()

    def endGame(self):
        self.bot.dropPrivateMsg(self)
        self.bot.dropPublicMsg(self)
        DangerousInvite.instance.games.pop(self.initServer.id)

    async def timeOut(self, time):
        await asyncio.sleep(time)
        self.endGame()
        if self.isTimeOut:
            await self.bot.send_message(self.initChannel, "타임아웃이에용! {}이(가) 설정한 금칙어: {}".format(self.initUser.mention, self.targetWord))
            try:
                await self.bot.kick(self.initUser)
            except Forbidden:
                await self.bot.send_message(self.initChannel, DangerousInvite.instance.errorMsg)
            image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data/dinvite"))
            with open("{}/dinvite_timeout.gif".format(image_path), "rb") as f:
                await self.bot.send_file(self.initChannel, f)


def setup(bot):
    dinvite = DangerousInvite(bot)
    bot.add_cog(dinvite)
