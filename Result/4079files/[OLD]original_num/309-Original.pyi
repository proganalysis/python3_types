# (generated with --quick)

from typing import Any, Callable, Sequence

logging: module
math: module
time: module

def retry_on_exception(tries: int = ..., delay: int = ..., backoff: int = ..., max_delay: int = ...) -> Callable[[Any], Any]: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
