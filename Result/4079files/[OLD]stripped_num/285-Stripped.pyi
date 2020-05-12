# (generated with --quick)

from typing import Any, Dict, TypeVar

logging: module

_T0 = TypeVar('_T0')

class Logging:
    __doc__: str
    kw: Dict[str, Any]
    def __enter__(self) -> logging.Logger: ...
    def __exit__(self, *exc) -> None: ...
    def __init__(self, **kw) -> None: ...

def logged(class_: _T0) -> _T0: ...
