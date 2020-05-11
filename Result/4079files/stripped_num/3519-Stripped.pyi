# (generated with --quick)

import __builtin__
import __future__
import io
from typing import Any, IO, Optional, Tuple, Type

BytesIO: Type[io.BytesIO]
Component: Any
SIZES: Tuple[Any, Any, Any, Any, Any]
absolute_import: __future__._Feature
b: Any
bm: Any
bytes: Any
chunker: Any
codecs: module
division: __future__._Feature
ids: set
iid: InstanceID
instance_id: InstanceID
int: Any
log: logging.Logger
logging: module
merkle: Any
print_function: __future__._Feature
proof: Any
proof_chain: Any
sample_bytes: Any
start_time: float
time: module
valid: bool
x: Any

class InstanceID(Any):
    CODE_MAX: str
    CODE_MIN: str
    __doc__: str
    merkle_tree: Any
    root: __builtin__.bytes
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def check_chain(chain) -> bool: ...
    @classmethod
    def from_data(cls, data, chunk_size = ..., bits = ...) -> Any: ...
    @classmethod
    def from_leaves(cls, leaves = ..., prehashed = ..., raw_digests = ..., bits = ...) -> Any: ...
    def get_chain(self, index) -> Any: ...
    def leaf_count(self) -> __builtin__.int: ...

def pprint(object: object, stream: Optional[IO[str]] = ..., indent: __builtin__.int = ..., width: __builtin__.int = ..., depth: Optional[__builtin__.int] = ..., *, compact: bool = ...) -> None: ...
