# (generated with --quick)

import json.decoder
import json.encoder
from typing import Any, Callable, List, Optional, Tuple, Type, Union

Namespace: Any
Operation: Any
Schema: Any
assert_that: Any
create_object_graph: Any
dump_response_data: Any
equal_to: Any
fields: Any
is_: Any
load_request_data: Any
request: Any
response: Any

class CommandArgumentSchema(Any):
    value: Any

class CommandResultSchema(Any):
    result: Any
    value: Any

class TestCommand:
    client: Any
    graph: Any
    ns: Any
    def setup(self) -> None: ...
    def test_command(self) -> None: ...
    def test_swagger(self) -> None: ...
    def test_url_for(self) -> None: ...

def dumps(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
def loads(s: Union[bytearray, bytes, str], encoding = ..., cls: Optional[Type[json.decoder.JSONDecoder]] = ..., object_hook: Optional[Callable[[dict], Any]] = ..., parse_float: Optional[Callable[[str], Any]] = ..., parse_int: Optional[Callable[[str], Any]] = ..., parse_constant: Optional[Callable[[str], Any]] = ..., object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ..., **kwds) -> Any: ...
def make_command(graph, ns, request_schema, response_schema) -> None: ...
