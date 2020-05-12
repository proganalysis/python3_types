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
    def form_response(self, itemid: int, defindex: int, paintindex: int, rarity: int, quality: int, paintwear: float, paintseed: int, inventory: int, origin: int, stattrak: int) -> str: ...
    def get_item(self, s: int, a: int, d: int, m: int) -> str: ...
    def send(self, s: int, a: int, d: int, m: int) -> Tuple[int, int, int, int, int, float, int, int, int, int]: ...
    def start(self, username: str, password: str) -> None: ...
