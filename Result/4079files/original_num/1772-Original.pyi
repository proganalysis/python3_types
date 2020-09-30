# (generated with --quick)

import decimal
import fractions
import functools
import itertools
import singledispatch
from typing import Any, Callable, List, Type, TypeVar, Union

CLASSES: List[str]
DECIMAL_PLACES: List[str]
Decimal: Type[decimal.Decimal]
Fraction: Type[fractions.Fraction]
HUNDREDS: List[str]
ONES: List[str]
TENS: List[str]
TEN_TO_TWENTY: List[str]
_: Callable[..., str]
_NORMALIZATION_TABLE: dict
_Union: Any
_chain: Type[itertools.chain]
words: Union[functools._SingleDispatchCallable[str], singledispatch._SingleDispatchCallable[str]]

_T = TypeVar('_T')

def _exp_words(number: str, positive: str, negative: str, decimal_separator: str, scientific_separator: str) -> str: ...
def _natural_words(str_num: str) -> str: ...
def _point_words(number: str, decimal_separator: str) -> str: ...
def _singledispatch(func: Callable[..., _T]) -> Union[functools._SingleDispatchCallable[_T], singledispatch._SingleDispatchCallable[_T]]: ...
def _three_digit_words(number: int) -> str: ...
def change_defaults(positive: str = ..., negative: str = ..., decimal_separator: str = ..., fraction_separator: str = ..., ordinal_denominator: bool = ..., scientific_separator: str = ...) -> None: ...
def ordinal_words(number: Union[int, str], positive: str = ..., negative: str = ...) -> str: ...
