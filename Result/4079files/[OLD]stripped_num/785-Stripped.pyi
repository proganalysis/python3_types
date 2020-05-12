# (generated with --quick)

from typing import Any

Stopper: Any
irt: Any
numpy: module

class MaxItemStopper(Any):
    __doc__: str
    _max_itens: Any
    def __init__(self, max_itens) -> None: ...
    def __str__(self) -> str: ...
    def stop(self, index = ..., administered_items = ..., **kwargs) -> Any: ...

class MinErrorStopper(Any):
    __doc__: str
    _min_error: Any
    def __init__(self, min_error) -> None: ...
    def __str__(self) -> str: ...
    def stop(self, index = ..., administered_items = ..., theta = ..., **kwargs) -> Any: ...
