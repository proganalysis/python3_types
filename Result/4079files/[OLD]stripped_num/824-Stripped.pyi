# (generated with --quick)

import collections
from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar, Union

PTCoefficientStandard = `namedtuple-PTCoefficientStandard-a-b-c`

Unit: Any
functools: module
noCorrection: Any
normalize_numeric: Any
normalize_temperature_celsius: Any
np: module
numbers: module
pt1000Correction: Any
pt1000_resistance: functools.partial[nothing]
pt1000_temperature: functools.partial[nothing]
pt100Correction: Any
pt100_resistance: functools.partial[nothing]
pt100_temperature: functools.partial[nothing]
ptxIPTS68: `namedtuple-PTCoefficientStandard-a-b-c`
ptxITS90: `namedtuple-PTCoefficientStandard-a-b-c`

_Tnamedtuple-PTCoefficientStandard-a-b-c = TypeVar('_Tnamedtuple-PTCoefficientStandard-a-b-c', bound=`namedtuple-PTCoefficientStandard-a-b-c`)

class `namedtuple-PTCoefficientStandard-a-b-c`(tuple):
    __slots__ = ["a", "b", "c"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    a: Any
    b: Any
    c: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-PTCoefficientStandard-a-b-c`], a, b, c) -> `_Tnamedtuple-PTCoefficientStandard-a-b-c`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-PTCoefficientStandard-a-b-c`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-PTCoefficientStandard-a-b-c`: ...
    def _replace(self: `_Tnamedtuple-PTCoefficientStandard-a-b-c`, **kwds) -> `_Tnamedtuple-PTCoefficientStandard-a-b-c`: ...

def checkCorrectionPolynomialQuality(r0, reftemp, poly) -> Tuple[Any, Any, Any]: ...
def computeCorrectionPolynomial(r0, order = ...) -> Any: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def ptx_resistance(r0, t, standard = ...) -> Any: ...
def ptx_temperature(r0, r, standard = ..., poly = ...) -> Any: ...
