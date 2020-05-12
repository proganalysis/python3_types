# (generated with --quick)

import inet
from typing import Any, Type

All: Any
Client: Type[inet.Client]
Optional: Any
Range: Any
Required: Any
port_def: Any
re: module
socket: module
time: module

class TCPClient(inet.Client):
    __doc__: str
    attr_name: str
    socket: socket.socket
    def __init__(self, port, timeout, tries, wait) -> None: ...
    def assert_receive(self, expected, timeout = ...) -> None: ...
    def assert_receive_regex(self, regex, timeout = ...) -> None: ...
    def close(self) -> None: ...
    def send(self, msg) -> None: ...
    @staticmethod
    def validator() -> dict: ...
