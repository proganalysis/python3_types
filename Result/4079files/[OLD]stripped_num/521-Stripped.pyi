# (generated with --quick)

import enum
from typing import Any, Tuple, Type

EBADF: int
ENOTCONN: int
Enum: Type[enum.Enum]
LOG: logging.Logger
SHUT_RDWR: int
SocketError: Type[OSError]
__all__: Tuple[str, str, str]
logging: module

class Connection:
    __doc__: str
    address: Any
    id: Tuple[Any, Any]
    port: Any
    protocol: ConnectionProtocol
    remaining_data: bytes
    socket: Any
    state: Any
    switch: Any
    def __init__(self, address, port, socket, switch = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def close(self) -> None: ...
    def is_alive(self) -> bool: ...
    def is_during_setup(self) -> Any: ...
    def is_established(self) -> Any: ...
    def is_new(self) -> Any: ...
    def send(self, buffer) -> None: ...
    def set_established_state(self) -> None: ...
    def set_setup_state(self) -> None: ...
    def update_switch(self, switch) -> None: ...

class ConnectionProtocol:
    __doc__: str
    name: Any
    state: Any
    version: Any
    def __init__(self, name = ..., version = ..., state = ...) -> None: ...

class ConnectionState(enum.Enum):
    ESTABLISHED: int
    FAILED: int
    FINISHED: int
    NEW: int
    SETUP: int
    __doc__: str
