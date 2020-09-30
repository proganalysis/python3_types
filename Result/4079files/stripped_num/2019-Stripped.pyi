# (generated with --quick)

from typing import Any, Dict, List, Optional, Tuple, TypeVar, Union

couchbaseConstants: Any
encodeCollectionId: Any
json: module
pump: Any
random: module
string: module
struct: module

_T1 = TypeVar('_T1')

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
    def can_handle(opts, spec) -> Any: ...
    @staticmethod
    def check(opts, spec: _T1) -> Tuple[Union[int, str], Optional[Dict[str, Union[Dict[Any, Union[float, int, str]], List[Dict[str, Union[str, List[Dict[str, str]]]]], _T1]]]]: ...
    @staticmethod
    def parse_spec(opts, spec) -> Tuple[Union[int, str], Optional[Dict[Any, Union[float, int, str]]]]: ...
    def provide_batch(self) -> Tuple[int, Any]: ...
    @staticmethod
    def provide_design(opts, source_spec, source_bucket, source_map) -> Tuple[int, None]: ...
    @staticmethod
    def total_msgs(opts, source_bucket, source_node, source_map) -> Tuple[int, Optional[int]]: ...
