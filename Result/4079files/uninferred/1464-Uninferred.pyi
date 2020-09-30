from ultros.networks.irc.connectors.base import BaseIRCConnector

__author__: str

class PlainIRCConnector(BaseIRCConnector):
    async def do_connect(self): ...
