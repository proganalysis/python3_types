# (generated with --quick)

import collections
import json.encoder
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

NOID: Any
OrderedDict: Type[collections.OrderedDict]

class ErrorResponse(JSONRPCResponse):
    __doc__: str
    code: Any
    data: Any
    id: Any
    jsonrpc: str
    message: Any
    ok: bool
    def __init__(self, error: Dict[str, Any], **kwargs) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class JSONRPCResponse:
    __doc__: str
    id: Any
    jsonrpc: str
    ok: bool
    def __init__(self, jsonrpc: str, id) -> None: ...

class NotificationResponse(SuccessResponse):
    __doc__: str
    id: Any
    jsonrpc: str
    ok: bool
    result: Any
    def __init__(self) -> None: ...

class Response:
    __doc__: str
    data: Optional[Union[JSONRPCResponse, List[JSONRPCResponse]]]
    raw: Any
    text: str
    def __init__(self, text: str, raw = ...) -> None: ...
    def __repr__(self) -> str: ...

class SuccessResponse(JSONRPCResponse):
    __doc__: str
    id: Any
    jsonrpc: str
    ok: bool
    result: Any
    def __init__(self, result, **kwargs) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

def serialize(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
def sort_response(response: Dict[str, Any]) -> collections.OrderedDict: ...
def total_results(data: Optional[Union[JSONRPCResponse, List[JSONRPCResponse]]], *, ok: bool = ...) -> int: ...
