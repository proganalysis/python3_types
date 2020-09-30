# (generated with --quick)

import threading
from typing import Any, Type

Lock: Type[threading.Lock]
Rpc: Any
json: module
log: logging.Logger
logging: module
ssl: module
websocket: Any

class Websocket(Any):
    _Websocket__lock: threading.Lock
    _request_id: int
    ws: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def connect(self) -> None: ...
    def disconnect(self) -> None: ...
    def rpcexec(self, payload) -> Any: ...
