# (generated with --quick)

from typing import Any, Dict, Optional, Tuple

couchbaseConstants: Any
encodeCollectionId: Any
json: module
pump: Any
random: module
string: module
struct: module

class GenSource(Any):
    __doc__: str
    body: Optional[str]
    cur_gets: Any
    cur_items: Any
    cur_ops: Any
    cur_sets: Any
    done: bool
    def __init__(self, opts, spec, source_bucket, source_node, source_map, sink_map, ctl, cur) -> None: ...
    @staticmethod
    def can_handle(opts, spec: str) -> bool: ...
    @staticmethod
    def check(opts, spec: str) -> Tuple[Any, Optional[Dict[str, Any]]]: ...
    @staticmethod
    def parse_spec(opts, spec: str) -> Tuple[Any, Optional[Dict[str, Any]]]: ...
    def provide_batch(self) -> Tuple[Any, Any]: ...
    @staticmethod
    def provide_design(opts, source_spec, source_bucket, source_map) -> Tuple[Any, Optional[str]]: ...
    @staticmethod
    def total_msgs(opts, source_bucket, source_node, source_map) -> Tuple[Any, Optional[int]]: ...
