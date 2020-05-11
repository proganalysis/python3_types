# (generated with --quick)

import asks.errors
import types
from typing import Any, Callable, Coroutine, Generator, List, Tuple, Type, TypeVar

BadStatus: Type[asks.errors.BadStatus]
SimpleNamespace: Type[types.SimpleNamespace]
_json: module
async_generator: Any
codecs: module
decompress: Callable
h11: Any
yield_: Any

_TStreamBody = TypeVar('_TStreamBody', bound=StreamBody)

class BaseResponse:
    __doc__: str
    body: Any
    cookies: List[nothing]
    encoding: Any
    headers: Any
    history: List[nothing]
    http_version: Any
    method: Any
    reason_phrase: Any
    status_code: Any
    url: Any
    def __aenter__(self) -> Coroutine[Any, Any, BaseResponse]: ...
    def __aexit__(self, *exc_info) -> Coroutine[Any, Any, None]: ...
    def __init__(self, encoding, http_version, status_code, reason_phrase, headers, body, method, url) -> None: ...
    def __repr__(self) -> str: ...
    def _decompress(self, encoding = ...) -> Any: ...
    def _guess_encoding(self) -> None: ...

class Cookie(types.SimpleNamespace):
    __doc__: str
    comment: None
    domain: None
    expires: None
    host: Any
    name: None
    path: None
    secure: bool
    value: None
    def __init__(self, host, data) -> None: ...
    def __iter__(self) -> Generator[Tuple[str, Any], Any, None]: ...

class Response(BaseResponse):
    body: Any
    content: Any
    cookies: List[nothing]
    encoding: Any
    headers: Any
    history: List[nothing]
    http_version: Any
    method: Any
    raw: Any
    reason_phrase: Any
    status_code: Any
    text: Any
    url: Any
    def json(self, **kwargs) -> Any: ...
    def raise_for_status(self) -> None: ...

class StreamBody:
    __aiter__: Any
    content_encoding: Any
    decompress_data: bool
    encoding: Any
    h11_connection: Any
    read_size: int
    sock: Any
    timeout: Any
    def __aenter__(self) -> Coroutine[Any, Any, StreamBody]: ...
    def __aexit__(self, *exc_info) -> Coroutine[Any, Any, None]: ...
    def __call__(self: _TStreamBody, timeout = ...) -> _TStreamBody: ...
    def __init__(self, h11_connection, sock, content_encoding = ..., encoding = ...) -> None: ...
    def _recv_event(self) -> coroutine: ...
    def close(self) -> Coroutine[Any, Any, None]: ...

class StreamResponse(BaseResponse):
    body: Any
    cookies: List[nothing]
    encoding: Any
    headers: Any
    history: List[nothing]
    http_version: Any
    method: Any
    reason_phrase: Any
    status_code: Any
    url: Any

def parse_content_encoding(content_encoding: str) -> Any: ...
def timeout_manager(timeout, coro, *args) -> coroutine: ...
