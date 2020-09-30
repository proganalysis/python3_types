import discord
from discord.ext import commands
from cogs.utils.session import Session, Page
from cogs.utils.http_handler import HTTPHandler
from bs4 import BeautifulSoup


class NSFW():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def 히토미(self, ctx, index):
        if not self.isNSFW(ctx.message.channel):
            await self.alertOnlyInNSFW(ctx.message.channel)
            return
        try:
            index = int(index)
        except ValueError:
            self.bot.say("제대로 된 숫자를 인자로 주세용")
            return
        await self.bot.send_typing(ctx.message.channel)
        url = "https://hitomi.la/galleries/{}.html".format(index)
        http = HTTPHandler()
        try:
            response = http.get(url, None)
        except Exception as e:
            await self.bot.say("페이지가 존재하지 않아용")
            return
        html = BeautifulSoup(response.read().decode(), 'html.parser')
        coverDiv = html.find("div", {"class": "cover"})
        coverUrl = "https:{}".format(coverDiv.find("img").get("src"))
        meta = html.find("div", {"class": "gallery"})
        title = self.getMetaInfo(meta.find("h1"))
        artist = self.getAllMetaInfo(meta.find("h2"))
        meta = meta.find("div", {"class": "gallery-info"})
        infoTypes = ["Group", "Type", "Language", "Series", "Characters", "Tags"]
        infoIsMultiple = [False, False, False, False, True, True]
        infoResults = []
        infoLists = meta.find_all("tr")
        for i in range(len(infoTypes)):
            info = infoLists[i]
            if infoIsMultiple[i]:
                infoResults.append(self.getAllMetaInfo(info.find_all("td")[1]))
            else:
                infoResults.append(self.getMetaInfo(info.find_all("td")[1]))
        em = discord.Embed(title=title, url=url, colour=0xDEADBF)
        em.set_image(url=coverUrl)
        em.add_field(name="Artist", value=artist)
        for i in range(len(infoTypes) - 1):
            em.add_field(name=infoTypes[i], value=infoResults[i])
        em.description = "Tags\n{}".format(infoResults[-1])

        msg = await self.bot.send_message(ctx.message.channel, embed=em)

        # Check Type
        if infoResults[1] == "anime":
            emojiMenu = ["❌"]
        else:
            emojiMenu = ["▶", "❌"]
        for emoji in emojiMenu:
            await self.bot.add_reaction(msg, emoji)

        res = await self.bot.wait_for_reaction(emojiMenu, timeout=30, user=ctx.message.author, message=msg)
        if not res:
            for emoji in emojiMenu:
                await self.bot.remove_reaction(msg, emoji, self.bot.user)
                await self.bot.remove_reaction(msg, emoji, ctx.message.author)
            return
        elif res.reaction.emoji == "▶":
            await self.bot.delete_message(msg)
            url = "https://hitomi.la/reader/{}.html".format(index)
            http = HTTPHandler()
            response = http.get(url, None)
            html = BeautifulSoup(response.read().decode(), 'html.parser')
            images = html.find_all("div", {"class": "img-url"})
            reader = discord.Embed(colour=0xDEADBF)
            reader.title = em.title
            reader.url = em.url
            await self.readHitomi(ctx.message, index, images, reader)
            return
        elif res.reaction.emoji == "❌":
            await self.bot.delete_message(msg)
            await self.bot.delete_message(ctx.message)
            return

    async def readHitomi(self, cmdMsg, index, images, em):
        images = [image.string for image in images]
        images = [image[image.rfind("/") + 1:] for image in images]

        if index % 2:
            url = "https://ba.hitomi.la/galleries/{}/{}"
        else:
            url = "https://aa.hitomi.la/galleries/{}/{}"

        images = [Page(image=url.format(index, image)) for image in images]
        session = Session(self.bot, cmdMsg, images, max_time=60, show_footer=True)
        await session.start()

    def isNSFW(self, channel):
        return channel.name.startswith("nsfw")

    def getMetaInfo(self, meta):
        aTag = meta.find('a')
        if aTag:
            return aTag.string.strip()
        else:
            string = meta.string
            if not string:
                string = "N/A"
            return string.strip()

    def getAllMetaInfo(self, meta):
        aTags = meta.find_all('a')
        if aTags:
            result = []
            for aTag in aTags:
                result.append(aTag.string.strip())
            return ", ".join(result)
        else:
            string = meta.string
            if not string:
                string = "N/A"
            return string.strip()

    async def alertOnlyInNSFW(self, channel):
        await self.bot.send_message(channel, "`nsfw`채널에서만 사용 가능한 명령어에용")


def setup(bot):
    cog = NSFW(bot)
    bot.add_cog(cog)
