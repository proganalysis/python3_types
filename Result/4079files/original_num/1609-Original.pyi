# (generated with --quick)

from typing import Callable, Iterable, List, TypeVar

_S = TypeVar('_S')
_T = TypeVar('_T')

class Solution:
    def reduce_func(self, nums: List[int]) -> int: ...
    def single_number(self, nums: List[int]) -> int: ...

@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
