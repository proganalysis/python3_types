# (generated with --quick)

import json.decoder
from typing import Any, Callable, List, Optional, Tuple, Type, Union

BatchResponse: Any
InvalidJSONRPCResponse: Any
InvalidJSONResponse: Any
JSONDecodeError: Type[json.decoder.JSONDecodeError]
Method: Any
Methods: Any
NOCONTEXT: Any
Request: Any
Response: Any
SuccessResponse: Any
ValidationError: Any
add_handlers: Any
apply_config: Any
asyncio: module
collections: module
config: Any
create_requests: Any
dispatch: Any
global_methods: Any
handle_exceptions: Any
log_request: Any
log_response: Any
remove_handlers: Any
schema: Any
validate: Any
validate_args: Any

def call(method, *args, **kwargs) -> coroutine: ...
def call_requests(requests, methods, debug: bool) -> coroutine: ...
def deserialize(s: Union[bytearray, bytes, str], encoding = ..., cls: Optional[Type[json.decoder.JSONDecoder]] = ..., object_hook: Optional[Callable[[dict], Any]] = ..., parse_float: Optional[Callable[[str], Any]] = ..., parse_int: Optional[Callable[[str], Any]] = ..., parse_constant: Optional[Callable[[str], Any]] = ..., object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ..., **kwds) -> Any: ...
def dispatch_pure(request: str, methods, *, context, convert_camel_case: bool, debug: bool) -> coroutine: ...
def safe_call(request, methods, *, debug: bool) -> coroutine: ...
