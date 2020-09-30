# (generated with --quick)

import contextlib
from typing import Any, List, Type, TypeVar, Union

ContextDecorator: Type[contextlib.ContextDecorator]
__all__: List[str]
sys: module
time: module

_TTimer = TypeVar('_TTimer', bound=Timer)

class Timer(contextlib.ContextDecorator):
    __doc__: str
    _elapsed: Union[float, int]
    _print_file: Any
    _print_title: Any
    _title: Any
    elapsed: Any
    start: float
    def __enter__(self: _TTimer) -> _TTimer: ...
    def __exit__(self, *args) -> None: ...
    def __float__(self) -> float: ...
    def __init__(self, title = ..., print_title = ..., print_file = ...) -> None: ...
