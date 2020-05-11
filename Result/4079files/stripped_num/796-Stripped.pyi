# (generated with --quick)

from typing import Any, Coroutine, Iterable, Mapping, Optional, Sequence, Tuple, Type, Union

Character: Any
Historical: Any
commands: Any
datetime: Type[datetime.datetime]
discord: Any
math: module
upload: Any

class Update:
    __doc__: str
    aap: Any
    all: Any
    ap: Any
    bot: Any
    dp: Any
    fame: Any
    lvl: Any
    pic: Any
    progress: Any
    update: Any
    def _Update__create_historical(self, character, date) -> Any: ...
    def _Update__get_member(self, author, user, server_id) -> Coroutine[Any, Any, Optional[Tuple[str, Any]]]: ...
    def __init__(self, bot) -> None: ...
    def update_attribute(self, ctx, attribute, user = ...) -> Coroutine[Any, Any, None]: ...

def __getattr__(name) -> Any: ...
def setup(bot) -> None: ...
def tabulate(tabular_data: Union[Iterable[Iterable], Mapping[str, Iterable]], headers: Union[str, Sequence[str]] = ..., tablefmt: Union[str, tabulate.TableFormat] = ..., floatfmt: Union[str, Iterable[str]] = ..., numalign: Optional[str] = ..., stralign: Optional[str] = ..., missingval: Union[str, Iterable[str]] = ..., showindex: Union[bool, Iterable] = ..., disable_numparse: Union[bool, Iterable[int]] = ..., colalign: Optional[Iterable[Optional[str]]] = ...) -> str: ...
