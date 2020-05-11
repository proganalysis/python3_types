# (generated with --quick)

import __builtin__
import functools
from typing import Any, Callable, Dict, Generator, List, Optional, Sequence, Tuple, Type, TypeVar, Union

BaseConfig: Any
ErrorList: Type[Union[ErrorWrapper, Sequence]]
__all__: Tuple[str, str]
get_exc_type: functools._lru_cache_wrapper[str]
json: module

_T = TypeVar('_T')

class ErrorWrapper:
    __slots__ = ["exc", "loc", "msg_template", "type_"]
    ctx: __builtin__.dict[str, Any]
    exc: Exception
    loc: Tuple[str, ...]
    msg: str
    msg_template: Any
    type_: str
    def __init__(self, exc: Exception, *, loc: Union[str, Tuple[str, ...]], config: Optional[type] = ...) -> None: ...
    def __repr__(self) -> str: ...
    def dict(self, *, loc_prefix: Optional[Tuple[str, ...]] = ...) -> __builtin__.dict[str, Any]: ...

class ValidationError(ValueError):
    __slots__ = ["model", "raw_errors"]
    errors: functools._lru_cache_wrapper[List[Dict[str, Any]]]
    model: Any
    raw_errors: Sequence[Union[ErrorWrapper, Sequence]]
    def __init__(self, errors: Sequence[Union[ErrorWrapper, Sequence]], model: type) -> None: ...
    def json(self, *, indent: Optional[Union[int, str]] = ...) -> str: ...

def _display_error_loc(error: Dict[str, Any]) -> str: ...
def _display_error_type_and_ctx(error: Dict[str, Any]) -> str: ...
def display_errors(errors: List[Dict[str, Any]]) -> str: ...
def flatten_errors(errors: Sequence, *, loc: Optional[Tuple[str, ...]] = ...) -> Generator[Dict[str, Any], None, None]: ...
def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
