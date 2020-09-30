# (generated with --quick)

from typing import Any, Callable

LOG: logging.Logger
base_numba: Any
logging: module
lp: Any
warnings: module

class NumbaCudaTarget(Any):
    def _wrap_dims(self, nbc_knl) -> Callable: ...
    def get_kernel_executor(self, knl, *args, **kwargs) -> Callable: ...
    def get_kernel_executor_cache_key(self, *args, **kwargs) -> str: ...

class NumbaTarget(Any):
    no_jit: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def get_kernel_executor(self, knl, *args, **kwargs) -> Any: ...
    def get_kernel_executor_cache_key(self, *args, **kwargs) -> str: ...
