# (generated with --quick)

import http.server
import threading
from typing import Any, Coroutine, Dict, Type

BaseDriver: Any
HTTPServer: Type[http.server.HTTPServer]
HttpDriver: Any
LimitRateDriverMixin: Any
MockServerRequestHandler: Any
SOCKS5DriverANONTestCase: Any
SOCKS5DriverAUTHTestCase: Any
Socks5Driver: Any
TCPConnector: Any
Thread: Type[threading.Thread]
URL: Any
aiosocks: Any
aiounittest: Any
asyncio: module
get_free_port: Any
json: module
math: module
mock: module
os: module
time: module

class HttpDirverTestCase(TestMethodsMixin, Any):
    driver_class: Any

class LimitRateBaseTestDriver(Any):
    def close(self) -> None: ...
    def json(self, *args, **kwargs) -> Coroutine[Any, Any, float]: ...

class LimitRateDriverMixinTestCase(Any):
    period: int
    requests_per_period: int
    def get_driver(self) -> LimitRateTestDriver: ...
    def test_json_fast(self) -> Coroutine[Any, Any, None]: ...
    def test_json_slow(self) -> Coroutine[Any, Any, None]: ...

class LimitRateTestDriver(Any, LimitRateBaseTestDriver):
    period: int
    requests_per_period: int

class TestMethodsMixin:
    driver_class: None
    driver_kwargs: Dict[nothing, nothing]
    json_filepath: str
    def get_bin(self, loop = ...) -> Coroutine[Any, Any, None]: ...
    def get_text(self, loop = ...) -> Coroutine[Any, Any, None]: ...
    def json(self, loop = ...) -> Coroutine[Any, Any, None]: ...
    def post_text(self, loop = ...) -> Coroutine[Any, Any, None]: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_get_bin_custom_loop(self) -> Coroutine[Any, Any, None]: ...
    def test_get_bin_default_loop(self) -> Coroutine[Any, Any, None]: ...
    def test_get_text_custom_loop(self) -> Coroutine[Any, Any, None]: ...
    def test_get_text_default_loop(self) -> Coroutine[Any, Any, None]: ...
    def test_json_custom_loop(self) -> Coroutine[Any, Any, None]: ...
    def test_json_default_loop(self) -> Coroutine[Any, Any, None]: ...
    def test_post_text_custom_loop(self) -> Coroutine[Any, Any, None]: ...
    def test_post_text_default_loop(self) -> Coroutine[Any, Any, None]: ...

class TestSocksConnector(Any):
    def __init__(self, proxy, proxy_auth, loop) -> None: ...
