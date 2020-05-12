from os.path import expanduser
from jsonpo.jsonpo import JSONPO
from jsonpo.jsonpo import JSONSD
import json


class Configure(JSONSD):
    """
    Configuration Manager
    ~/.stats-notes/auth.json
    if not exists create a new file and directory in the Home directory
    """

    FilePath = expanduser("~") + "/.stats-notes/auth.json"

    def __init__(self, filepath = None):
        self.autologin = None
        self.Manager = JSONPO(Configure.FilePath)
        self.Manager.load(self)
        if filepath is not None:
            Configure.FilePath = filepath

    def __serialize__(self):
        return json.dumps({
            "config": {
                "autologin": self.autologin
            }
        })

    def __deserialize__(self, obj):
        self.autologin = obj["config"]["autologin"]

    def get_auto_login(self):
        return self.autologin

    def set_auto_login(self, autlogin):
        self.autologin = autlogin
        self.Manager.save(self)

    def save(self):
        self.Manager.save(self)
