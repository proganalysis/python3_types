# (generated with --quick)

from typing import Any, Coroutine, Type

File: Any
SocksConnector: Any
aiofiles: Any
aiohttp: Any
asyncio: module
datetime: Type[datetime.datetime]
filetype: Any
logger: Any
os: module
ssl: module

class BaseConnection:
    active: bool
    app: Any
    connect_task: None
    friend: Any
    pause_time: int
    running: bool
    ssl_context: ssl.SSLContext
    def __init__(self, app, friend) -> None: ...
    def connect(self) -> Coroutine[Any, Any, None]: ...
    def get_file(self, path, range = ...) -> coroutine: ...
    def offer_file(self, path) -> Coroutine[Any, Any, None]: ...
    def ping(self) -> Coroutine[Any, Any, nothing]: ...
    def restart_connection(self) -> None: ...
    def send(self, message) -> Coroutine[Any, Any, bool]: ...

class DirectConnection(BaseConnection):
    active: bool
    app: Any
    connect_task: None
    friend: Any
    host: Any
    pause_time: int
    ping_task: None
    running: bool
    session: Any
    ssl_context: ssl.SSLContext
    def __str__(self) -> str: ...
    def _connect(self) -> Coroutine[Any, Any, None]: ...

class TorConnection(BaseConnection):
    active: bool
    app: Any
    connect_task: None
    friend: Any
    host: Any
    pause_time: int
    running: bool
    session: Any
    ssl_context: ssl.SSLContext
    def __str__(self) -> str: ...
    def _connect(self) -> Coroutine[Any, Any, None]: ...
