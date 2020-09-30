# (generated with --quick)

import io
from typing import Any, Dict, Type, TypeVar

StringIO: Type[io.StringIO]

_TColorizer = TypeVar('_TColorizer', bound=Colorizer)

class Colorizer:
    __doc__: str
    codes: Dict[str, str]
    modifiers: Any
    reset: str
    sep: str
    template: str
    def __call__(self, *args, sep = ..., end = ..., reset = ...) -> str: ...
    def __getattr__(self: _TColorizer, name) -> _TColorizer: ...
    def __init__(self, modifiers = ...) -> None: ...
    def print(self, *args, sep = ..., end = ..., file = ..., flush = ...) -> None: ...

def sprint(*values, sep = ..., end = ...) -> str: ...
