# (generated with --quick)

import _ast
import _csv
from typing import Any, Dict, List, Optional, TextIO, Tuple, TypeVar, Union

couchbaseConstants: Any
csv: module
json: module
logging: module
os: module
pump: Any
snappy: Any
struct: module
sys: module
urllib: module

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')

class CSVSink(Any):
    CSV_JSON_SCHEME: str
    CSV_SCHEME: str
    __doc__: str
    csvfile: Optional[TextIO]
    fields: Optional[list]
    writer: Optional[_csv._writer]
    def __init__(self, opts, spec, source_bucket, source_node, source_map, sink_map, ctl, cur) -> None: ...
    def bucket_name(self) -> Any: ...
    @staticmethod
    def can_handle(opts, spec) -> bool: ...
    @staticmethod
    def check(opts, spec, source_map) -> Tuple[Any, None]: ...
    def close(self) -> None: ...
    def consume_batch_async(self, batch) -> Tuple[Union[int, str], Any]: ...
    @staticmethod
    def consume_design(opts, sink_spec, sink_map, source_bucket, source_map, source_design) -> int: ...
    def convert_meta(self, meta) -> Any: ...
    def get_csvfile(self, base) -> Any: ...
    def node_name(self) -> Any: ...

class CSVSource(Any):
    __doc__: str
    done: bool
    fields: List[str]
    r: Optional[_csv._reader]
    def __init__(self, opts, spec, source_bucket, source_node, source_map, sink_map, ctl, cur) -> None: ...
    @staticmethod
    def can_handle(opts, spec) -> Any: ...
    @staticmethod
    def check(opts, spec: _T1) -> Tuple[int, Dict[str, Union[List[Dict[str, Any]], _T1]]]: ...
    def provide_batch(self) -> Tuple[Union[int, str], Any]: ...
    @staticmethod
    def provide_design(opts, source_spec, source_bucket, source_map) -> Tuple[int, None]: ...

def literal_eval(node_or_string: Union[str, _ast.AST]) -> Any: ...
def number_try_parse(s: _T0) -> Union[float, int, _T0]: ...
