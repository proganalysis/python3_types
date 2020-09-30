# (generated with --quick)

import contextlib
import types
from typing import Any, Callable, Iterator, Optional, Tuple, Type, TypeVar

logger: logging.Logger
logging: module
re: module
sweeten_errors: Callable[..., contextlib._GeneratorContextManager]
term: Any

_T = TypeVar('_T')

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def exc_info() -> Tuple[Optional[Type[BaseException]], Optional[BaseException], Optional[types.TracebackType]]: ...
