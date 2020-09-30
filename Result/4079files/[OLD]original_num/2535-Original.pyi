# (generated with --quick)

from typing import Any, Coroutine, NoReturn

ATTR_AUTH_TOKEN: Any
ATTR_CLIENT_AUTH: Any
AsyncConnection: Any
FakeConnectionHmip: Any
FakeLookupHmip: Any
FakeWebsocketHmip: Any
HmipConnectionError: Any
HmipServerCloseError: Any
HmipWrongHttpStatusError: Any
aiohttp: Any
asyncio: module
fake_lookup_server: Any
fake_server: Any
fake_websocket_server: Any
mockreturn: Any
pytest: Any
test_init: Any
test_post_200: Any
test_post_200_no_json: Any
test_post_404: Any
test_post_404_alt: Any
test_post_exhaustive_timeout: Any
test_websocket_exhaustive_timeout: Any

def do_test(future, loop, url, base_url = ...) -> Coroutine[Any, Any, None]: ...
def finish_all(loop) -> None: ...
def start_async_client_connection(connector, loop, base_url, url) -> coroutine: ...
def start_fake_server(loop, base_url) -> coroutine: ...
def test_ws_client_shutdown() -> None: ...
def test_ws_message() -> None: ...
def test_ws_ping_pong() -> None: ...
def test_ws_recover() -> NoReturn: ...
def test_ws_server_shutdown() -> None: ...
def ws_listen(future, connection) -> Coroutine[Any, Any, None]: ...
