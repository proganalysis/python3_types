# (generated with --quick)

import asyncio.events
from typing import Any, Callable, Coroutine, Dict, Mapping, Optional, Sequence, Tuple, TypeVar, Union
import urllib.parse

Cookies: Any
MultiDict: Any
Packet: Any
QueryDict: Any
TCPIo: Any
_loop: Optional[asyncio.events.AbstractEventLoop]
asyncio: module
json: module
res: ClientResponse
ssl: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T = TypeVar('_T')
_TEnvironment = TypeVar('_TEnvironment', bound=Environment)

class ClientResponse(object):
    _body: Any
    cookie: Dict[Any, dict]
    cookies: None
    header: Optional[dict]
    json: Any
    raw: Any
    reason: str
    status: int
    txt: Any

class Environment(object):
    data: Any
    headers: Any
    query: Any
    def __init__(self, query = ..., data = ..., headers = ...) -> None: ...
    def copy(self: _TEnvironment) -> _TEnvironment: ...

class RequestTimeoutException(Exception): ...

def _read_response(conn) -> Coroutine[Any, Any, ClientResponse]: ...
def _task_wrapper(future, conn) -> Coroutine[Any, Any, None]: ...
def _timeout_handler(future, task) -> None: ...
def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def fetch(method: str, url: str, query: Optional[dict] = ..., data = ..., headers: Optional[dict] = ..., env: Optional[Environment] = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., timeout: float = ...) -> Coroutine[Any, Any, ClientResponse]: ...
def get_loop() -> Any: ...
@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
def set_loop(loop: asyncio.events.AbstractEventLoop) -> None: ...
def urlencode(query: Union[Mapping, Sequence[Tuple[Any, Any]]], doseq: bool = ..., safe: AnyStr = ..., encoding: str = ..., errors: str = ..., quote_via: Callable[[str, AnyStr, str, str], str] = ...) -> str: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
