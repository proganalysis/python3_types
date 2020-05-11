# (generated with --quick)

import collections
import functools
from typing import Any, Callable, Iterable, Optional, Sized, Tuple, Type, TypeVar, Union

TimeReport = `namedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`
TimeSignature = `namedtuple-TimeSignature-top-bottom`

Clock: Any
iprint: Any
seconds_per_tick: functools._lru_cache_wrapper
synchronized: Any
ticks_per_measure: functools._lru_cache_wrapper

_T = TypeVar('_T')
_Tnamedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing = TypeVar('_Tnamedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing', bound=`namedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`)
_Tnamedtuple-TimeSignature-top-bottom = TypeVar('_Tnamedtuple-TimeSignature-top-bottom', bound=`namedtuple-TimeSignature-top-bottom`)

class `namedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`(tuple):
    __slots__ = ["bpm", "delta", "measure", "playing", "prog", "signature", "tick"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str, str]
    bpm: Any
    delta: Any
    measure: Any
    playing: Any
    prog: Any
    signature: Any
    tick: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`], delta, measure, signature, tick, bpm, prog, playing) -> `_Tnamedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`: ...
    def _replace(self: `_Tnamedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`, **kwds) -> `_Tnamedtuple-TimeReport-delta-measure-signature-tick-bpm-prog-playing`: ...

class `namedtuple-TimeSignature-top-bottom`(tuple):
    __slots__ = ["bottom", "top"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    bottom: Any
    top: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-TimeSignature-top-bottom`], top, bottom) -> `_Tnamedtuple-TimeSignature-top-bottom`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-TimeSignature-top-bottom`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-TimeSignature-top-bottom`: ...
    def _replace(self: `_Tnamedtuple-TimeSignature-top-bottom`, **kwds) -> `_Tnamedtuple-TimeSignature-top-bottom`: ...

def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def time() -> float: ...
