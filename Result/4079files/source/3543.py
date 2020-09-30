import discord
import urllib
import json
from discord.ext import commands
from random import randint
from cogs.utils.observable import Observable
from cogs.utils.http_handler import HTTPHandler
from cogs.utils.session import Session, Page, AuthorInfo


class GG2(Observable):
    def __init__(self, bot):
        self.bot = bot
        self.bot.listenPublicMsg(self)

    async def update(self, message):
        await self.checkGG2Bubble(message)

    async def checkGG2Bubble(self, message):
        content = message.content.lower()
        length = len(content)
        if content in ["센트리", "우버", 'e']:
            with open("./data/gg2/{}.png".format(content), "rb") as f:
                await self.bot.send_file(message.channel, f)
        elif content == 'f':
            taunt = "{}{}".format(content, randint(0, 9))
            with open("./data/gg2/{}.png".format(taunt), "rb") as f:
                await self.bot.send_file(message.channel, f)
        elif 0 < length <= 3:
            if content[0] in ['z', 'c', 'f']:
                if length != 2:
                    return
                if 49 <= ord(content[1]) <= 57:
                    with open("./data/gg2/{}.png".format(content), "rb") as f:
                        await self.bot.send_file(message.channel, f)
            elif content[0] == 'x':
                try:
                    num = int(content[1:])
                    if 0 <= num <= 29:
                        with open("./data/gg2/{}.png".format(content), "rb") as f:
                            await self.bot.send_file(message.channel, f)
                except Exception:
                    return

    @commands.command(pass_context=True)
    async def 갱게서버(self, ctx):
        GG2_LOBBY_URL = "http://www.ganggarrison.com/lobby/status"
        http = HTTPHandler()
        response = http.get(GG2_LOBBY_URL, None)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read().decode()
            serverList = self.findServerList(response_body)
            em = discord.Embed(title="현재 GG2 로비 정보에용", colour=0xDEADBF)
            for server in serverList:
                personPercentage = server.current / server.max
                if personPercentage < 0.33:
                    personEmoji = "☠️"
                elif personPercentage < 0.66:
                    personEmoji = "🙇"
                else:
                    personEmoji = "🙌"
                desc = "🗺️: {}\n🛠️: {}\n{}: {}/{}".format(server.map, server.mod, personEmoji, server.current, server.max)
                em.add_field(name="💠 {}".format(server.name), value=desc)
            await self.bot.send_message(ctx.message.channel, embed=em)
        else:
            await self.bot.say("오류가 발생했어용\n{}".format(response.read().decode("utf-8")))

    def findServerList(self, body):
        serverList = []
        serverTable = body.find("<tbody>")
        if serverTable == -1:
            return
        serverNext = body.find("<tr>", serverTable) + 1

        def findNextCell(body, startIndex):
            return body.find("<td>", startIndex + 1)

        def getCellContent(body, startIndex):
            endIndex = body.find("</td>", startIndex)
            cell = body[startIndex + 4:endIndex]
            return cell

        while (serverNext > 0):
            server = ServerInfo()
            cell = findNextCell(body, serverNext)  # Exclude Blank Cell

            cell = findNextCell(body, cell)  # Name
            server.name = getCellContent(body, cell)

            cell = findNextCell(body, cell)  # Map
            server.map = getCellContent(body, cell)

            cell = findNextCell(body, cell)  # PlayerInfo
            playerInfo = getCellContent(body, cell).split("/")
            server.current = int(playerInfo[0])
            server.max = int(playerInfo[1])

            cell = findNextCell(body, cell)  # Mod
            modInfo = getCellContent(body, cell)
            modStart = modInfo.find(">") + 1
            modEnd = modInfo.rfind("</a>")
            server.mod = modInfo[modStart:modEnd]
            serverList.append(server)

            serverNext = body.find("<tr>", serverNext) + 1

        return serverList

    @commands.command(pass_context=True)
    async def 갱게스텟(self, ctx, *args):
        if len(args) == 0:
            await self.bot.say("닉네임도 주세용")
            return
        nickname = " ".join([arg for arg in args])
        nickname = urllib.parse.quote(nickname.encode("utf-8"))
        url = "http://gg2statsapp.appspot.com/getstat?nickname={}".format(nickname)

        http = HTTPHandler()
        response = http.get(url, None)
        rescode = response.getcode()
        if not rescode == 200:
            await self.bot.say("오류가 발생했어용: {}".format(rescode))
            return

        response_body = response.read().decode()
        stat = json.loads(response_body)
        if not stat:
            await self.bot.say("해당 유저의 정보가 없어용")
            return

        pages = []
        pages.append(self.overall(stat))
        pages.append(self.playtime(stat))
        pages.append(self.classinfo(stat))

        session = Session(self.bot, ctx.message, pages=pages, show_footer=True)
        await session.start()

    def overall(self, stat):
        nickname = stat["nickname"]
        encodedNickname = urllib.parse.quote(nickname.encode("utf-8"))
        region = stat["region"][:2].lower()
        kda = (stat["kill"] + stat["assist"]) / max(stat["death"], 1)
        h, m, d = self.parseTime(stat["time_total"])

        thumb = "http://gg2statsapp.appspot.com/avatar?nickname={}".format(encodedNickname)

        desc = []
        desc.append(":flag_{}:".format(region))
        if stat["title"]:
            desc.append("\"{}\"".format(stat["title"]))
        desc.append("`LEVEL` **{}** `EXP` **{}** / **{}** `COIN` **{}**".format(stat["level"], stat["exp"], self.maxExp(stat["level"]), stat["coin"]))
        desc.append("**{}**시간 **{}**분 **{}**초동안 **{}**판 플레이".format(h, m, d, stat["playcount"]))
        desc.append("🔫: **{}**, 💀: **{}**, 🤝: **{}**, `KDA`: **{:.2f}**".format(stat["kill"], stat["death"], stat["assist"], kda))
        desc.append("🚩: **{}**, 🛡️: **{}**, 💥: **{}**".format(stat["capture"], stat["defense"], stat["destruction"]))
        desc.append("🗡️: **{}**, ♥️: **{}**, 🌟: **{}**".format(stat["stab"], self.strlize(stat["healing"]), stat["invuln"]))
        desc.append("**{}**`승` **{}**`패` **{}**`비김` **{}**`탈주`".format(stat["win"], stat["lose"], stat["draw"], stat["disconnect"]))
        desc = "\n".join(desc)
        author = AuthorInfo(
            name="{}{}의 스텟 정보에용".format(stat["clan"], nickname),
            url="http://gg2statsapp.appspot.com/profile?id={}".format(encodedNickname),
            icon_url="http://gg2statsapp.appspot.com/avatar?nickname={}".format(encodedNickname)
        )
        return Page(desc=desc, authorInfo=author, thumb=thumb, footer_format="종합정보(%index/%total)")

    def playtime(self, stat):
        nickname = stat["nickname"]
        encodedNickname = urllib.parse.quote(nickname.encode("utf-8"))

        red = int(stat["time_red"] * 100 / stat["time_total"])
        blue = int(stat["time_blue"] * 100 / stat["time_total"])
        spec = int(stat["time_spectate"] * 100 / stat["time_total"])

        redStr = self.timeToString(self.parseTime(stat["time_red"]))
        blueStr = self.timeToString(self.parseTime(stat["time_blue"]))
        specStr = self.timeToString(self.parseTime(stat["time_spectate"]))

        chartUrl = ["https://image-charts.com/chart?cht=p"]
        chartUrl.append("chtt={}'s+Playtime".format(stat["nickname"]))
        chartUrl.append("chs=300x300")
        chartUrl.append("chd=t:{},{},{}".format(red, blue, spec))
        chartUrl.append("chl={}|{}|{}".format(redStr, blueStr, specStr))
        chartUrl.append("chds=a")
        chartUrl.append("chdl=Red|Blue|Spectate")
        chartUrl.append("chco=FF6347,4169E1,757575")
        chartUrl = "&".join(chartUrl)

        author = AuthorInfo(
            name="{}{}의 스텟 정보에용".format(stat["clan"], nickname),
            url="http://gg2statsapp.appspot.com/profile?id={}".format(encodedNickname),
            icon_url="http://gg2statsapp.appspot.com/avatar?nickname={}".format(encodedNickname)
        )
        return Page(image=chartUrl, authorInfo=author, footer_format="플레이타임(%index/%total)")

    def classinfo(self, stat):
        nickname = stat["nickname"]
        encodedNickname = urllib.parse.quote(nickname.encode("utf-8"))
        classes = ["runner", "firebug", "rocketman", "overweight", "detonator", "healer", "constructor", "infiltrator", "rifleman", "quote"]

        killData = []
        for cls in classes:
            killData.append(str(stat["{}_kill".format(cls)]))
        killData = ",".join(killData)

        deathData = []
        for cls in classes:
            deathData.append(str(stat["{}_death".format(cls)]))
        deathData = ",".join(deathData)

        assistData = []
        for cls in classes:
            assistData.append(str(stat["{}_assist".format(cls)]))
        assistData = ",".join(assistData)

        classData = [killData, deathData, assistData]
        classData = "|".join(classData)

        chartUrl = ["https://image-charts.com/chart?cht=bhs"]
        chartUrl.append("chs=600x300")
        chartUrl.append("chd=t:{}".format(classData))
        chartUrl.append("chdl=Kill|Death|Assist")
        chartUrl = "&".join(chartUrl)

        author = AuthorInfo(
            name="{}{}의 스텟 정보에용".format(stat["clan"], nickname),
            url="http://gg2statsapp.appspot.com/profile?id={}".format(encodedNickname),
            icon_url="http://gg2statsapp.appspot.com/avatar?nickname={}".format(encodedNickname)
        )
        return Page(image=chartUrl, authorInfo=author, footer_format="클래스별 정보(%index/%total)")

    def parseTime(self, user_time):
        time_h = 0
        time_m = 0
        time_s = 0
        if user_time // 108000:
            time_h = user_time // 108000
            user_time -= 108000 * time_h
        if user_time // 1800 and time_h < 100:
            time_m = user_time // 1800
            user_time -= 1800 * time_m
        if not time_h:
            time_s = user_time // 30
        return (time_h, time_m, time_s)

    def timeToString(self, timeInfo):
        result = []
        h, m, s = timeInfo
        if h > 0:
            result.append("{}h".format(h))
        if h < 100:
            result.append("{}m".format(m))
        if h <= 0:
            result.append("{}s".format(s))
        return "+".join(result)

    def maxExp(self, level):
        return 1500 * level

    def strlize(self, num):
        if (num >= 1000):
            return "{:.1f}K".format(num / 1000)
        elif (num >= 1000000):
            return "{:.1f}M".format(num / 1000000)
        else:
            return "{:.1f}".format(num)


class ServerInfo:
    def __init__(self):
        self.name = None
        self.map = None
        self.mod = None
        self.current = None
        self.max = None


def setup(bot):
    cog = GG2(bot)
    bot.add_cog(cog)
