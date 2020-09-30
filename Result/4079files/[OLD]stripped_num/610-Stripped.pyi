# (generated with --quick)

import setting_parser
from typing import Any, Type
import wsgiref.simple_server

CURREN_DIR: str
SETTINGS: str
SettingsParser: Type[setting_parser.SettingsParser]
application: Any
falcon: Any
logging: module
os: module
server: wsgiref.simple_server.WSGIServer
simple_server: module
sys: module
uuid: module

class Pull(object):
    __doc__: str
    logger: logging.Logger
    settings_parser: setting_parser.SettingsParser
    def on_get(self, req, resp, boxid) -> None: ...
