# (generated with --quick)

import __builtin__
import abc
import enum
from typing import Any, Callable, Tuple, Type, TypeVar, Union

ABCMeta: Type[abc.ABCMeta]
Enum: Type[enum.Enum]
__all__: Tuple[str, str, str, str]
operator: module

_FuncT = TypeVar('_FuncT', bound=Callable)
_TDelta = TypeVar('_TDelta', bound=Delta)

class ChangeDelta(Delta):
    __doc__: str
    original: Chunk
    revised: Chunk
    type: Any

class Chunk:
    __slots__ = ["lines", "position"]
    __doc__: str
    last: Any
    lines: Any
    position: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, position, lines) -> None: ...
    def __len__(self) -> int: ...
    def verify(self, target) -> None: ...

class DeleteDelta(Delta):
    __doc__: str
    original: Chunk
    revised: Chunk
    type: Any

class Delta(metaclass=abc.ABCMeta):
    __slots__ = ["original", "revised"]
    Type: __builtin__.type
    __doc__: str
    original: Chunk
    revised: Chunk
    type: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, original: Chunk, revised: Chunk) -> None: ...
    def apply_to(self, target) -> None: ...
    @staticmethod
    def create(original: Chunk, revised: Chunk) -> Delta: ...
    def restore(self, target) -> None: ...
    def reverse(self: _TDelta) -> _TDelta: ...
    def verify(self, target) -> None: ...

class InsertDelta(Delta):
    __doc__: str
    original: Chunk
    revised: Chunk
    type: Any

class Patch:
    __doc__: str
    _deltas: Union[list, tuple]
    deltas: Tuple[Delta, ...]
    def __eq__(self, other) -> Any: ...
    def __init__(self) -> None: ...
    def add_delta(self, delta) -> None: ...
    def apply_to(self, target) -> list: ...
    def restore(self, target) -> list: ...

class PatchFailedException(Exception):
    __doc__: str

def abstractmethod(callable: _FuncT) -> _FuncT: ...
