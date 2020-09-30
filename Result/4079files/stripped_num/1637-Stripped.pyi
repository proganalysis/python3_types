# (generated with --quick)

import sqlite3.dbapi2
from typing import Any, Tuple

CSGOClient: Any
ECsgoGCMsg: Any
LOG: logging.Logger
SteamClient: Any
const: Any
json: module
logging: module
sqlite3: module
struct: module

class CSGOWorker(object):
    connection: sqlite3.dbapi2.Connection
    csgo: Any
    cursor: sqlite3.dbapi2.Cursor
    logon_details: None
    request_method: Any
    response_method: Any
    steam: Any
    def cli_login(self) -> None: ...
    def close(self) -> None: ...
    def form_response(self, itemid, defindex, paintindex, rarity, quality, paintwear, paintseed, inventory, origin, stattrak) -> str: ...
    def get_item(self, s, a, d, m) -> str: ...
    def send(self, s, a, d, m) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any, int]: ...
    def start(self, username, password) -> None: ...
