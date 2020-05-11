# (generated with --quick)

import enum
from typing import Any, Type, TypeVar

Enum: Type[enum.Enum]
IntFlag: Type[enum.IntFlag]

_T0 = TypeVar('_T0')

class Com(enum.IntFlag):
    C: int
    E: int
    F: int
    N: int
    NE: int
    NW: int
    S: int
    SE: int
    SW: int
    W: int
    X: int

class Dim:
    x: Any
    y: Any
    z: Any
    def __cmp__(self, other) -> Any: ...
    def __init__(self, x = ..., y = ..., z = ...) -> None: ...
    def __str__(self) -> str: ...

class Orientation(enum.Enum):
    EW: bool
    NS: bool

class Reverse:
    reverse_map: Any
    def __call__(self, enum: _T0) -> _T0: ...
    def __init__(self, reverse_map) -> None: ...
