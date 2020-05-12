# (generated with --quick)

import flask.app
from typing import Any, Coroutine, Type, TypeVar
import werkzeug.routing

PathConverter: Type[werkzeug.routing.PathConverter]
WebSocketProtocol: Any
app: Any
asyncio: module
client: Any
flask: module
json: module
logging: module
mock_service: Any
pytest: Any
sanic: Any
sanic_sentry: module
sanic_server: Any
sentry_calls: Any
sentry_mock: Any
sentry_url: Any
test_exception: Any
threading: module
websocket_client: Any
zlib: module

_TService = TypeVar('_TService', bound=Service)

class EverythingConverter(werkzeug.routing.PathConverter):
    regex: str

class Service:
    app: flask.app.Flask
    host: Any
    port: Any
    server_thread: threading.Thread
    srv: Any
    url: str
    def __enter__(self: _TService) -> _TService: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, *, host, port) -> None: ...
    def __repr__(self) -> str: ...
    def run(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

def make_server(host = ..., port = ..., app = ..., threaded: bool = ..., processes: int = ..., request_handler = ..., passthrough_errors: bool = ..., ssl_context = ..., fd = ...) -> Any: ...
def test_error_handler(app, client, sentry_calls, sentry_url) -> Coroutine[Any, Any, None]: ...
def test_exception_in_error_handler(app, client, sentry_calls, sentry_url) -> Coroutine[Any, Any, None]: ...
def test_simple(app, client, sentry_url, sentry_calls) -> Coroutine[Any, Any, None]: ...
def test_warning(app, client, sentry_calls, sentry_url) -> Coroutine[Any, Any, None]: ...
def test_warning_not_sent(app, client, sentry_calls, sentry_url) -> Coroutine[Any, Any, None]: ...
def test_websocket(app, websocket_client, sentry_calls, sentry_url) -> Coroutine[Any, Any, None]: ...
def test_websocket_exception(app, websocket_client, sentry_calls, sentry_url) -> Coroutine[Any, Any, None]: ...
