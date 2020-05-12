# (generated with --quick)

from typing import Any, Optional

Stopper: Any
irt: Any
numpy: module

class MaxItemStopper(Any):
    __doc__: str
    _max_itens: int
    def __init__(self, max_itens: int) -> None: ...
    def __str__(self) -> str: ...
    def stop(self, index: Optional[int] = ..., administered_items: Optional[numpy.ndarray] = ..., **kwargs) -> bool: ...

class MinErrorStopper(Any):
    __doc__: str
    _min_error: float
    def __init__(self, min_error: float) -> None: ...
    def __str__(self) -> str: ...
    def stop(self, index: Optional[int] = ..., administered_items: Optional[numpy.ndarray] = ..., theta: Optional[float] = ..., **kwargs) -> bool: ...
