# (generated with --quick)

import abc
import asks.cookie_utils
import asks.errors
import asks.req_structs
import functools
from typing import Any, Callable, Coroutine, List, Optional, Sequence, Tuple, Type, TypeVar, Union
import urllib.parse

ABCMeta: Type[abc.ABCMeta]
BadHttpResponse: Type[asks.errors.BadHttpResponse]
CookieTracker: Type[asks.cookie_utils.CookieTracker]
RemoteProtocolError: Any
RequestProcessor: Any
SocketQ: Type[asks.req_structs.SocketQ]
__all__: List[str]
connect_tcp: Any
create_semaphore: Any
partialmethod: Type[functools.partialmethod]
ssl: module

AnyStr = TypeVar('AnyStr', str, bytes)
_FuncT = TypeVar('_FuncT', bound=Callable)
_T = TypeVar('_T')

class BaseSession(metaclass=abc.ABCMeta):
    __doc__: str
    _cookie_tracker: None
    delete: Callable
    encoding: None
    get: Callable
    head: Callable
    headers: Any
    options: Callable
    post: Callable
    put: Callable
    sema: Any
    source_address: None
    ssl_context: Any
    def __init__(self, headers = ..., ssl_context = ...) -> None: ...
    def _connect(self, host_loc) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    @abstractmethod
    def _grab_connection(self, url) -> coroutine: ...
    def _handle_exception(self, e, sock) -> Coroutine[Any, Any, None]: ...
    @abstractmethod
    def _make_url(self) -> Any: ...
    def _open_connection_http(self, location) -> coroutine: ...
    def _open_connection_https(self, location) -> coroutine: ...
    def request(self, method, url = ..., *, path = ..., retries = ..., connection_timeout = ..., **kwargs) -> coroutine: ...
    @abstractmethod
    def return_to_pool(self, sock) -> coroutine: ...

class Session(BaseSession):
    __doc__: str
    _conn_pool: asks.req_structs.SocketQ
    _connections: Any
    _cookie_tracker: Any
    _sema: None
    base_location: Any
    encoding: Any
    endpoint: Any
    headers: Any
    sema: Any
    source_address: None
    ssl_context: Any
    def __aenter__(self) -> Coroutine[Any, Any, Session]: ...
    def __aexit__(self, exc_type, exc_value, traceback) -> Coroutine[Any, Any, None]: ...
    def __init__(self, base_location = ..., endpoint = ..., headers = ..., encoding = ..., persist_cookies = ..., ssl_context = ..., connections = ...) -> None: ...
    def _checkout_connection(self, host_loc) -> Any: ...
    def _grab_connection(self, url) -> coroutine: ...
    def _make_connection(self, host_loc) -> coroutine: ...
    def _make_url(self) -> Any: ...
    def close(self) -> Coroutine[Any, Any, None]: ...
    def return_to_pool(self, sock) -> Coroutine[Any, Any, None]: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
def copy(x: _T) -> _T: ...
def get_netloc_port(scheme, netloc) -> Tuple[Any, Any]: ...
def timeout_manager(timeout, coro, *args) -> coroutine: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
def urlunparse(components: Union[Sequence[Optional[AnyStr]], Tuple[Optional[AnyStr], Optional[AnyStr], Optional[AnyStr], Optional[AnyStr], Optional[AnyStr], Optional[AnyStr]]]) -> AnyStr: ...
