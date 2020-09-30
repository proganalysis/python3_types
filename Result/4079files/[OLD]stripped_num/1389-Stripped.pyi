# (generated with --quick)

import json.decoder
from typing import Any, Coroutine, Dict, Type

JSONDecodeError: Type[json.decoder.JSONDecodeError]
aiohttp: Any
checks: Any
commands: Any
dataIO: Any
datetime: Type[datetime.datetime]
discord: Any
hashlib: module
os: module
send_cmd_help: module

class Smite:
    __doc__: str
    _auth_smite: Any
    _nameclear_smite: Any
    _nameset_smite: Any
    _ping_smite: Any
    _stats_smite: Any
    bot: Any
    header: Dict[str, str]
    settings: Any
    settings_path: str
    smite: Any
    url_pc: str
    def __init__(self, bot) -> None: ...
    def create_session(self) -> Coroutine[Any, Any, bool]: ...
    def league_tier(self, tier) -> str: ...
    def ping(self) -> Coroutine[Any, Any, None]: ...
    def test_session(self) -> Coroutine[Any, Any, bool]: ...

def check_files() -> None: ...
def check_folders() -> None: ...
def setup(bot) -> None: ...
