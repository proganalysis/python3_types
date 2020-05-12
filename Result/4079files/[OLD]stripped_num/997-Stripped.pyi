# (generated with --quick)

from typing import Any, Callable, Iterable, TypeVar

BitVector: Any
PythonSimulator: Any
m: Any
mantle: Any
simulator: Any

_S = TypeVar('_S')
_T = TypeVar('_T')

class SimpleALU(Any):
    IO: list
    name: str
    @classmethod
    def definition(io) -> None: ...

def one_hot_mux(conds, inputs) -> Any: ...
@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
