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
_: Callable
_NORMALIZATION_TABLE: dict
_Union: Any
_chain: Type[itertools.chain]
words: Union[functools._SingleDispatchCallable, singledispatch._SingleDispatchCallable]

_T = TypeVar('_T')

def _exp_words(number, positive, negative, decimal_separator, scientific_separator) -> Any: ...
def _natural_words(str_num) -> str: ...
def _point_words(number, decimal_separator) -> Any: ...
def _singledispatch(func: Callable[..., _T]) -> Union[functools._SingleDispatchCallable[_T], singledispatch._SingleDispatchCallable[_T]]: ...
def _three_digit_words(number) -> Any: ...
def change_defaults(positive = ..., negative = ..., decimal_separator = ..., fraction_separator = ..., ordinal_denominator = ..., scientific_separator = ...) -> None: ...
def ordinal_words(number, positive = ..., negative = ...) -> Any: ...
