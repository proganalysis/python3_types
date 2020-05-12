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
    app: str
    config: Any
    debug: bool
    manager: Any
    middleware: List[Callable[..., Awaitable[None]]]
    server: Any
    signal: Any
    signal_manager: Any
    def __init__(self, name: str = ...) -> None: ...
    def close_server_async(self) -> Coroutine[Any, Any, None]: ...
    def handler(self, request) -> Coroutine[Any, Any, Tuple[int, str, List[Tuple[str, str]], bytes]]: ...
    def run(self, host: str = ..., port: int = ..., debug: bool = ...) -> None: ...
    def start_server(self, host: str, port: int = ...) -> Coroutine[Any, Any, None]: ...
    def use(self, *middleware: Callable[..., Awaitable[None]]) -> None: ...
