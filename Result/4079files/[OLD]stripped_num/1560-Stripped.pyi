# (generated with --quick)

from typing import Any, Coroutine, Tuple

CIMultiDict: Any
CIMultiDictProxy: Any
ProxyConnector: Any
aiohttp: Any
aiosocks: Any
hdrs: Any

class BaseDriver:
    _loop: Any
    timeout: Any
    def __init__(self, timeout = ..., loop = ...) -> None: ...
    def close(self) -> Coroutine[Any, Any, nothing]: ...
    def get_bin(self, url, params, timeout = ...) -> Coroutine[Any, Any, nothing]: ...
    def get_text(self, url, params, timeout = ...) -> Coroutine[Any, Any, nothing]: ...
    def json(self, url, params, timeout = ...) -> Coroutine[Any, Any, nothing]: ...
    def post_text(self, url, data, timeout = ...) -> Coroutine[Any, Any, nothing]: ...

class CustomClientResponse(Any):
    headers: Any
    raw_headers: tuple
    def start(self, connection, read_until_eof = ...) -> Coroutine[Any, Any, CustomClientResponse]: ...

class HttpDriver(BaseDriver):
    _loop: Any
    session: Any
    timeout: Any
    def __init__(self, timeout = ..., loop = ..., session = ...) -> None: ...
    def close(self) -> Coroutine[Any, Any, None]: ...
    def get_bin(self, url, params, timeout = ...) -> coroutine: ...
    def get_text(self, url, params, timeout = ...) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def json(self, url, params, timeout = ...) -> coroutine: ...
    def post_text(self, url, data, timeout = ...) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...

class Socks5Driver(HttpDriver):
    _loop: Any
    connector: Any
    session: Any
    timeout: Any
    def __init__(self, address, port, login = ..., password = ..., timeout = ..., loop = ...) -> None: ...
