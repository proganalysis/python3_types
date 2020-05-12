# (generated with --quick)

import __future__
from typing import Any, Callable, Generator, Iterable, Tuple, TypeVar, Union

_ValueType = Iterable[Union[int, str]]

_PARENT_INDEX_COLUMN: str
_SLICE_KEY_COLUMN: str
absolute_import: __future__._Feature
arrow_util: Any
collections: module
constants: Any
division: __future__._Feature
functools: module
merge: Any
pa: Any
pd: Any
print_function: __future__._Feature
six: module
stats_util: Any
types: Any

_T0 = TypeVar('_T0')

def _to_slice_key(feature_value) -> Any: ...
def default_slicer(table: _T0) -> Generator[Tuple[Any, _T0], Any, None]: ...
def generate_slices(table, slice_functions, **kwargs) -> Generator[Any, Any, None]: ...
def get_feature_value_slicer(features) -> Callable[[Any], Any]: ...
