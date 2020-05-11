# (generated with --quick)

from typing import Any, List, Optional, Union

Addstatus: Any
BaseCommand: Any
CommandError: Any
getAuth: Any
getConfig: Any
json: module
logger: logging.Logger
logging: module
os: module
setup_logging: Any
stat: Any
tweepy: Any

class Command(Any):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...

def isfile(path: Union[_PathLike, bytes, str]) -> bool: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
@overload
def listdir(path: bytes) -> List[bytes]: ...
@overload
def listdir(path: Optional[str] = ...) -> List[str]: ...
@overload
def listdir(path: Union[int, _PathLike[str]]) -> List[str]: ...
