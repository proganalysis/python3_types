# (generated with --quick)

from typing import Any, Callable, Sequence

logging: module
math: module
time: module

def retry_on_exception(tries = ..., delay = ..., backoff = ..., max_delay = ...) -> Callable[[Any], Any]: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
