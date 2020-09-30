# (generated with --quick)

import threading
import typing
from typing import Any, Type

MutableMapping: Type[typing.MutableMapping]
RLock: Type[threading._RLock]
check_argument_types: Any
load: Any
sentinel: Any
traverse: Any

class lazy:
    __doc__: Any
    func: Any
    lock: threading._RLock
    def __get__(self, instance, type = ...) -> Any: ...
    def __init__(self, func, name = ..., doc = ...) -> None: ...
    def __repr__(self) -> str: ...

def lazyload(reference, *args, **kw) -> lazy: ...
