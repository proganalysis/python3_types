# (generated with --quick)

import __builtin__
import __future__
import builtins
import numpy
from typing import Any, Callable, Iterable, Iterator, List, Tuple, Type, TypeVar, Union

Client: Any
backend: __builtin__.str
c: Any
cb: Any
coo_matrix: Any
cse: Any
division: __future__._Feature
dview: Any
f_rate: Any
f_rates: numpy.ndarray
ffll: Any
fls: List[__builtin__.str]
folder_in: Any
folders: numpy.ndarray
imread: Any
mpl: Any
n_processes: Any
np: module
old_div: Any
os: module
params: List[List[Union[float, __builtin__.str]]]
pars: List[List[nothing]]
pl: Any
plt: Any
print_function: __future__._Feature
psutil: Any
res: list
scipy: Any
single_thread: bool
str: Type[builtins.str]
subprocess: module
sys: module
tifffile: Any
tm: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T = TypeVar('_T')
_T0 = TypeVar('_T0')
_T2 = TypeVar('_T2')

def create_images_for_labeling(pars: _T0) -> Union[Exception, _T0]: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
@overload
def map(function, *sequences: Iterable[nothing]) -> Iterator[nothing]: ...
@overload
def map(function: Callable[..., _T], *sequences: Iterable) -> Iterator[_T]: ...
def processor_placeholder(pars) -> Any: ...
def time() -> float: ...
@overload
def zip() -> Iterator[nothing]: ...
@overload
def zip(seq1, seq2, seq3, *seqs: Iterable) -> Iterator[tuple]: ...
@overload
def zip(seq1: Iterable, seq2: Iterable[nothing]) -> Iterator[nothing]: ...
@overload
def zip(seq1: Iterable[nothing], seq2: Iterable) -> Iterator[nothing]: ...
@overload
def zip(seq1: Iterable[_T]) -> Iterator[Tuple[_T]]: ...
@overload
def zip(seq1: Iterable[_T], seq2: Iterable[_T2]) -> Iterator[Tuple[_T, _T2]]: ...
