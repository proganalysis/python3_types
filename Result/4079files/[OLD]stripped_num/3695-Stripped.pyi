# (generated with --quick)

from typing import Any, Awaitable, Callable, Coroutine, List, Tuple

MiddlewareType = Callable[..., Awaitable[None]]

ALLOWED_SIGNALS: List[str]
Config: Any
HttpException: Any
Manager: Any
Request: Any
Response: Any
Signal: Any
asyncio: module
empty: Any
is_middleware: Any
map_context_to_middleware: Any
serve: Any

class Nougat:
    app: Any
    config: Any
    debug: Any
    manager: Any
    middleware: list
    server: Any
    signal: Any
    signal_manager: Any
    def __init__(self, name = ...) -> None: ...
    def close_server_async(self) -> Coroutine[Any, Any, None]: ...
    def handler(self, request) -> Coroutine[Any, Any, Tuple[Any, Any, Any, Any]]: ...
    def run(self, host = ..., port = ..., debug = ...) -> None: ...
    def start_server(self, host, port = ...) -> Coroutine[Any, Any, None]: ...
    def use(self, *middleware) -> None: ...
