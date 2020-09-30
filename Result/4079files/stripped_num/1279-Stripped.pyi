# (generated with --quick)

from typing import Any, Callable, Sequence

ColoredFormatter: Any
logger: logging.Logger
logging: module

def exception_logger(func) -> Callable: ...
def make_logger(name, fname = ...) -> logging.Logger: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
