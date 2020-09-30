# (generated with --quick)

import __builtin__
import functools
from typing import Any, Callable, Generator, Optional, Sequence, Tuple, Type, TypeVar, Union

BaseConfig: Any
ErrorList: Type[Union[ErrorWrapper, Sequence]]
__all__: Tuple[str, str]
get_exc_type: functools._lru_cache_wrapper
json: module

_T = TypeVar('_T')

class ErrorWrapper:
    __slots__ = ["exc", "loc", "msg_template", "type_"]
    ctx: Any
    exc: Any
    loc: Any
    msg: Any
    msg_template: Any
    type_: Any
    def __init__(self, exc, *, loc, config = ...) -> None: ...
    def __repr__(self) -> str: ...
    def dict(self, *, loc_prefix = ...) -> __builtin__.dict[str, Any]: ...

class ValidationError(ValueError):
    __slots__ = ["model", "raw_errors"]
    errors: functools._lru_cache_wrapper
    model: Any
    raw_errors: Any
    def __init__(self, errors, model) -> None: ...
    def json(self, *, indent = ...) -> Any: ...

def _display_error_loc(error) -> str: ...
def _display_error_type_and_ctx(error) -> str: ...
def display_errors(errors) -> str: ...
def flatten_errors(errors, *, loc = ...) -> Generator[Any, Any, None]: ...
def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
