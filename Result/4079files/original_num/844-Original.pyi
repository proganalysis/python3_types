# (generated with --quick)

import threading
import typing
from typing import Any, Callable, Optional, Type

MutableMapping: Type[typing.MutableMapping]
RLock: Type[threading._RLock]
check_argument_types: Any
load: Any
sentinel: Any
traverse: Any

class lazy:
    __doc__: str
    func: Callable[[Any], None]
    lock: threading._RLock
    def __get__(self, instance, type = ...) -> Any: ...
    def __init__(self, func: Callable[[object], None], name: Optional[str] = ..., doc: Optional[str] = ...) -> None: ...
    def __repr__(self) -> str: ...

def lazyload(reference: str, *args, **kw) -> lazy: ...
