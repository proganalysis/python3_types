# (generated with --quick)

import _weakref
import asyncio.locks
from typing import Any, Coroutine, Type

Event: Type[asyncio.locks.Event]
abc: module
logging: module
re: module
weakref: module

class BaseAccessor(object):
    CHECK_CONFIG: bool
    DEFAULT_HOST: str
    DEFAULT_PASSWORD: None
    DEFAULT_PORT: None
    DEFAULT_USERNAME: None
    _connected_event: asyncio.locks.Event
    _host: Any
    _password: Any
    _port: Any
    _store: _weakref.ReferenceType[nothing]
    _username: Any
    config: Any
    connected: bool
    connecting: bool
    debug: Any
    disconnecting: bool
    fingerprint: str
    has_credentials: bool
    host: Any
    logger: logging.Logger
    loop: Any
    password: Any
    port: Any
    store: Any
    type: Any
    username: Any
    def __init__(self, config, type, store, loop = ...) -> None: ...
    @abstractmethod
    def _connect(self) -> Coroutine[Any, Any, None]: ...
    @abstractmethod
    def _disconnect(self) -> Coroutine[Any, Any, None]: ...
    def check_config(self) -> None: ...
    def connect(self) -> Coroutine[Any, Any, None]: ...
    def disconnect(self) -> Coroutine[Any, Any, None]: ...
    def wait_connected(self) -> Coroutine[Any, Any, bool]: ...

class BaseAccessorException(Exception): ...

class ConfigurationError(Exception): ...
