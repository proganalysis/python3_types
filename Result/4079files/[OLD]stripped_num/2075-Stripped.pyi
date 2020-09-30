# (generated with --quick)

import collections
from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar, Union

Point = `namedtuple-Point-x-y`

Point_3D: Any
p: Tuple[nothing, ...]
p1: `namedtuple-Point-x-y`
p1_a: Point_a
p2: `namedtuple-Point-x-y`
p2_a: Point_a
p_3d: Any
p_a: Point_a
p_d: collections.OrderedDict[str, Any]
p_new: `namedtuple-Point-x-y`

_TPoint_a = TypeVar('_TPoint_a', bound=Point_a)
_Tnamedtuple-Point-x-y = TypeVar('_Tnamedtuple-Point-x-y', bound=`namedtuple-Point-x-y`)
_Tnamedtuple-Point_a-x-y = TypeVar('_Tnamedtuple-Point_a-x-y', bound=`namedtuple-Point_a-x-y`)

class Point_a(`namedtuple-Point_a-x-y`):
    def __add__(self: _TPoint_a, other) -> _TPoint_a: ...

class `namedtuple-Point-x-y`(tuple):
    __slots__ = ["x", "y"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    x: Any
    y: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Point-x-y`], x, y) -> `_Tnamedtuple-Point-x-y`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Point-x-y`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Point-x-y`: ...
    def _replace(self: `_Tnamedtuple-Point-x-y`, **kwds) -> `_Tnamedtuple-Point-x-y`: ...

class `namedtuple-Point_a-x-y`(tuple):
    __slots__ = ["x", "y"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    x: Any
    y: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Point_a-x-y`], x, y) -> `_Tnamedtuple-Point_a-x-y`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Point_a-x-y`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Point_a-x-y`: ...
    def _replace(self: `_Tnamedtuple-Point_a-x-y`, **kwds) -> `_Tnamedtuple-Point_a-x-y`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
