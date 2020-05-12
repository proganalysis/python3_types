# (generated with --quick)

from typing import Any, Callable, Iterable, TypeVar

_S = TypeVar('_S')
_T = TypeVar('_T')

class Solution:
    def reduce_func(self, nums) -> Any: ...
    def single_number(self, nums) -> Any: ...

@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
