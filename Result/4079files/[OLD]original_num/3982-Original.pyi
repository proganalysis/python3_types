# (generated with --quick)

from typing import Any, Callable

cached: Any
contextmod: module
exceptions: module
functools: module
raise_if_nothing_inferred: Any
util: module
wrapt: module
yes_if_nothing_inferred: Any

class cachedproperty:
    __slots__ = ["wrapped"]
    __doc__: str
    def __get__(self, inst, objtype = ...) -> Any: ...
    def __init__(self, wrapped) -> None: ...
    def wrapped(self, _1) -> Any: ...

def path_wrapper(func) -> Callable: ...
