# (generated with --quick)

from typing import Any, Coroutine, Dict, Optional, Type, TypeVar

aiohttp: Any
checks: Any
commands: Any
dataIO: Any
datetime: Type[datetime.datetime]
discord: Any
log: logging.Logger
logging: module
os: module

AnyStr = TypeVar('AnyStr', str, bytes)

class GithubCards:
    __author__: str
    __doc__: str
    __version__: str
    add: Any
    bot: Any
    colour: Dict[str, int]
    edit: Any
    githubcards: Any
    ignore: bool
    list: Any
    remove: Any
    settings: Any
    def __init__(self, bot) -> None: ...
    def get_issue(self, message) -> Coroutine[Any, Any, Optional[bool]]: ...
    def post_issue(self, message, prefix, number) -> Coroutine[Any, Any, Optional[bool]]: ...
    def save_json(self) -> None: ...

def check_file() -> None: ...
def check_folder() -> None: ...
def fnmatch(name: AnyStr, pat: AnyStr) -> bool: ...
def setup(bot) -> None: ...
