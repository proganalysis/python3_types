# (generated with --quick)

import itertools
import typing
from typing import Any, Iterator, Tuple, Type, TypeVar

Iterable: Type[typing.Iterable]
ParameterGrid: Any
Sized: Type[typing.Sized]
_get_matching_items: Any
chain: Type[itertools.chain]
list_intersection: Any
pytest: Any
rm_dups: Any

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_T6 = TypeVar('_T6')

@overload
def product(iter1: typing.Iterable, iter2: typing.Iterable, iter3: typing.Iterable, iter4: typing.Iterable, iter5: typing.Iterable, iter6: typing.Iterable, iter7: typing.Iterable, *iterables: Iterable) -> Iterator[tuple]: ...
@overload
def product(iter1: typing.Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def product(iter1: typing.Iterable[_T1], iter2: typing.Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def product(iter1: typing.Iterable[_T1], iter2: typing.Iterable[_T2], iter3: typing.Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def product(iter1: typing.Iterable[_T1], iter2: typing.Iterable[_T2], iter3: typing.Iterable[_T3], iter4: typing.Iterable[_T4]) -> Iterator[Tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def product(iter1: typing.Iterable[_T1], iter2: typing.Iterable[_T2], iter3: typing.Iterable[_T3], iter4: typing.Iterable[_T4], iter5: typing.Iterable[_T5]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def product(iter1: typing.Iterable[_T1], iter2: typing.Iterable[_T2], iter3: typing.Iterable[_T3], iter4: typing.Iterable[_T4], iter5: typing.Iterable[_T5], iter6: typing.Iterable[_T6]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
@overload
def product(*iterables: Iterable, repeat: int = ...) -> Iterator[tuple]: ...
def test_get_matching_items() -> None: ...
def test_list_intersection() -> None: ...
def test_parameter_grid() -> None: ...
def test_remove_duplicates() -> None: ...
