# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
Cell: Any
HIDDEN: Any
NORMAL: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class Mover(object, metaclass=abc.ABCMeta):
    __metaclass__: Type[abc.ABCMeta]
    body: None
    canvases: list
    goal: None
    halo: None
    ids: list
    is_miner: bool
    levels: int
    maze: Any
    offset: Any
    size: Any
    track: list
    def __init__(self, maze) -> None: ...
    @abstractmethod
    def _run(self) -> Any: ...
    def cell(self) -> None: ...
    def dig(self, cell) -> None: ...
    def finished(self) -> Any: ...
    def go(self, cell) -> None: ...
    def run(self) -> None: ...
    def tk_init(self, maze) -> None: ...
    def tk_move(self, dim) -> None: ...
    def tk_paint(self) -> None: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
