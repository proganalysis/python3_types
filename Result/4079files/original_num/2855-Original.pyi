# (generated with --quick)

from typing import Any, Dict, List, Sequence, TypeVar

CHAR_DOWN: List[str]
CHAR_MID: List[str]
CHAR_UP: List[str]
asyncio: module
commands: Any
dataIO: Any
default_settings: Dict[str, int]
discord: Any
os: module
send_cmd_help: module

_T = TypeVar('_T')

class Zalgo:
    __doc__: str
    bot: Any
    down: Any
    intensity: Any
    mid: Any
    settings: Any
    up: Any
    view: Any
    zalgo: Any
    zalgoset: Any
    def __init__(self, bot) -> None: ...
    def _zalgo_(self, text: str, settings) -> str: ...

def check_files() -> None: ...
def check_folders() -> None: ...
def choice(seq: Sequence[_T]) -> _T: ...
def setup(bot) -> None: ...
