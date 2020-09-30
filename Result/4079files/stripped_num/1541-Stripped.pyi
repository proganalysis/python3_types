# (generated with --quick)

import functools
from typing import Any, Callable, Dict, Optional, SupportsFloat, TypeVar, Union

AllOps: Any
DummyPlatform: Any
ForceDirectedScheduler: Any
HlsAllocator: Any
HlsScheduler: Any
ListSchedueler: Any
OpRealizationMeta: Any
_OPS_T_GROWING_CONST: set
_OPS_T_GROWING_EXP: set
_OPS_T_GROWING_LIN: set

_T = TypeVar('_T')

class VirtualHlsPlatform(Any):
    _OP_DELAYS: Dict[Any, Union[float, int]]
    __doc__: str
    allocator: Any
    get_op_realization: functools._lru_cache_wrapper
    scheduler: Any
    def __init__(self) -> None: ...
    def onHlsInit(self, hls) -> None: ...

def log2(__x: SupportsFloat) -> float: ...
def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
