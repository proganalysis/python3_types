# (generated with --quick)

from typing import Any, Coroutine

s_base: Any
s_common: Any

class Share(Any):
    __doc__: str
    entered: bool
    exited: bool
    iden: Any
    item: Any
    link: Any
    orig: Any
    def __anit__(self, link, item) -> Coroutine[Any, Any, None]: ...
    def _runShareLoop(self) -> Coroutine[Any, Any, None]: ...
