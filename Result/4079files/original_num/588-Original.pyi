# (generated with --quick)

from typing import Any, Callable, Sequence

ArgumentError: Any
Attribute: Any
RewritingError: Any
Sort: Any
identity: Any

class Strategy(Any): ...

class fixpoint(Strategy):
    f: Any
    def __call__(self, terms) -> Any: ...

class try_(Strategy):
    f: Any
    def __call__(self, terms) -> set: ...

class union(Strategy):
    left: Any
    right: Any
    def __call__(self, terms) -> Any: ...
    def __init__(self, *operands) -> None: ...

def make_strategy(fn) -> Any: ...
def set_operation(fn) -> Callable: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
