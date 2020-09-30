# (generated with --quick)

from typing import Any, Coroutine, Iterable, List, Mapping, Optional, Sequence, Union

asyncio: module
checks: Any
commands: Any
copy: module
dataIO: Any
discord: Any
log: logging.Logger
logging: module
os: module
send_cmd_help: module
time: module

class Punish:
    __author__: str
    __doc__: str
    __version__: str
    bot: Any
    day: List[str]
    hour: List[str]
    json: Any
    location: str
    min: List[str]
    muted: Any
    punish: Any
    task: Any
    unpunish: Any
    def _Punish__unload(self) -> None: ...
    def __init__(self, bot) -> None: ...
    def _timestamp(self, t, unit) -> Any: ...
    def check_time(self) -> coroutine: ...
    def new_channel(self, c) -> Coroutine[Any, Any, None]: ...
    def new_member(self, member) -> Coroutine[Any, Any, None]: ...

def check_file() -> None: ...
def check_folder() -> None: ...
def setup(bot) -> None: ...
def tabulate(tabular_data: Union[Iterable[Iterable], Mapping[str, Iterable]], headers: Union[str, Sequence[str]] = ..., tablefmt: Union[str, tabulate.TableFormat] = ..., floatfmt: Union[str, Iterable[str]] = ..., numalign: Optional[str] = ..., stralign: Optional[str] = ..., missingval: Union[str, Iterable[str]] = ..., showindex: Union[bool, Iterable] = ..., disable_numparse: Union[bool, Iterable[int]] = ..., colalign: Optional[Iterable[Optional[str]]] = ...) -> str: ...
