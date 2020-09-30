import json
import datetime
from pathlib import Path
from dateutil.relativedelta import relativedelta


class MilitaryInfo:
    def __init__(self):
        self.path = "military_info.json"
        self.servers = dict()

    def setData(self, serverId, key, value):
        targetServer = self.servers.get(serverId)
        if not targetServer:
            targetServer = dict()
            self.servers[serverId] = targetServer
        targetServer[key] = value
        self.save()

    def load(self):
        file = Path(self.path)
        if not file.is_file():
            return
        with open(self.path) as info:
            encodedDict = json.load(info)
            for serverHash in encodedDict:
                serverInfo = encodedDict[serverHash]
                self.servers[serverHash] = dict()
                server = self.servers[serverHash]
                for name in serverInfo:
                    personInfo = serverInfo[name]
                    encodedDate = personInfo["startDate"]
                    encodedDate = [int(i) for i in encodedDate.split("/")]
                    encodedDate = datetime.date(encodedDate[0], encodedDate[1], encodedDate[2])
                    if personInfo["class"] == "Military":
                        server[name] = Military(encodedDate)
                    elif personInfo["class"] == "Airforce":
                        server[name] = Airforce(encodedDate)
                    elif personInfo["class"] == "PublicService":
                        server[name] = PublicService(encodedDate)

    def save(self):
        f = open(self.path, "w")
        infoToDump = {}
        for serverId in self.servers:
            serverInfo = self.servers[serverId]
            serverDump = {}
            infoToDump[serverId] = serverDump
            for name in serverInfo:
                serverDump[name] = serverInfo[name].encode()
        f.write(json.dumps(infoToDump))
        f.close()


class Military:
    def __init__(self, startDate):
        self.startDate = startDate

    def getStartDate(self):
        return self.startDate

    def getDischargeDate(self):
        return self.startDate + relativedelta(months=18, days=-1)

    def getEmojiSet(self):
        return ("💖", "🖤")

    def getSymbol(self):
        return "🔫"

    def encode(self):
        return {"class": "Military", "startDate": self.startDate.strftime("%Y/%m/%d")}


class Airforce(Military):
    def getDischargeDate(self):
        return self.startDate + relativedelta(months=24, days=-1)

    def getEmojiSet(self):
        return ("🏇", "🐎")

    def getSymbol(self):
        return "✈️"

    def encode(self):
        return {"class": "Airforce", "startDate": self.startDate.strftime("%Y/%m/%d")}


class PublicService(Military):
    def getEmojiSet(self):
        return ("💖", "🖤")

    def encode(self):
        return {"class": "PublicService", "startDate": self.startDate.strftime("%Y/%m/%d")}
