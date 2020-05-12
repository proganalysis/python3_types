# (generated with --quick)

import __future__
from typing import Any

Compression: Any
_allreduce: Any
absolute_import: __future__._Feature
allgather: Any
broadcast: Any
check_extension: Any
division: __future__._Feature
init: Any
local_rank: Any
local_size: Any
mpi_threads_supported: Any
print_function: __future__._Feature
rank: Any
size: Any
tf: Any

class BroadcastGlobalVariablesHook(Any):
    __doc__: str
    bcast_op: Any
    device: Any
    root_rank: Any
    def __init__(self, root_rank, device = ...) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def begin(self) -> None: ...

class DistributedOptimizer(Any):
    __doc__: str
    _compression: Any
    _device_dense: Any
    _device_sparse: Any
    _optimizer: Any
    def __init__(self, optimizer, name = ..., use_locking = ..., device_dense = ..., device_sparse = ..., compression = ...) -> None: ...
    def apply_gradients(self, *args, **kwargs) -> Any: ...
    def compute_gradients(self, *args, **kwargs) -> Any: ...
    def get_slot(self, *args, **kwargs) -> Any: ...
    def get_slot_names(self, *args, **kwargs) -> Any: ...
    def variables(self, *args, **kwargs) -> Any: ...

def allreduce(tensor, average = ..., device_dense = ..., device_sparse = ..., compression = ...) -> Any: ...
def broadcast_global_variables(root_rank) -> Any: ...
