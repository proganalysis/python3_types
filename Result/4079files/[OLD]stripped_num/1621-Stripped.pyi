# (generated with --quick)

from typing import Any, Generator, List, TypeVar, Union

CursorKind: Any
TypeKind: Any
_builtin_types: list
pydoc: module
re: module
sys: module

_T0 = TypeVar('_T0')

def desugar_type(t) -> Any: ...
def get_fully_qualified_name(c) -> Any: ...
def import_class(cls_name) -> Any: ...
def is_builtin_type(t) -> bool: ...
def name_argument(name: _T0, index) -> Union[str, _T0]: ...
def sanitize_symbol(symbol) -> str: ...
def split_arguments() -> Generator[List[str], Any, None]: ...
