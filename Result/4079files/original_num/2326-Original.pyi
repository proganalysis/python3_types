# (generated with --quick)

from typing import Any

Network: Any
Service: Any

class NetworkService(Any):
    _service: Any
    available: Any
    connected: Any
    def __init__(self, device, uuid) -> None: ...
    def connect(self, reply_handler = ..., error_handler = ...) -> None: ...
    def disconnect(self, reply_handler = ..., error_handler = ..., *args) -> None: ...
