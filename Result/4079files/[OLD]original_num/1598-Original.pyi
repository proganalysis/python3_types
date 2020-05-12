# (generated with --quick)

import __builtin__
import __future__
from typing import Any, Callable, Iterable, Iterator, Optional, Tuple, Type, TypeVar
import unittest.case

Unit: Any
absolute_import: __future__._Feature
as_unit: Any
copy: module
division: __future__._Feature
print_function: __future__._Feature
range: Type[__builtin__.range]
unittest: module

_T = TypeVar('_T')
_T2 = TypeVar('_T2')

class StubUnit(object):
    calendar: Optional[str]
    category: int
    origin: str
    ut_unit: int
    def __init__(self, calendar = ...) -> None: ...

class TestAll(unittest.case.TestCase):
    def _assert_unit_equal(self, unit1, unit2) -> None: ...
    def test_cf_unit(self) -> None: ...
    def test_non_cf_unit_no_calendar(self) -> None: ...
    def test_non_cf_unit_with_calendar(self) -> None: ...

def filter(function: Optional[Callable[[_T], Any]], iterable: Iterable[_T]) -> Iterator[_T]: ...
def input(prompt: str = ...) -> str: ...
@overload
def map(function, *sequences: Iterable[nothing]) -> Iterator[nothing]: ...
@overload
def map(function: Callable[..., _T], *sequences: Iterable) -> Iterator[_T]: ...
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
