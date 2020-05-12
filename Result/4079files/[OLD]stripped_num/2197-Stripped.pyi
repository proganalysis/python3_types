# (generated with --quick)

from typing import Any

BaseTerminal: Any
paramiko: Any

class SshTerminal(Any):
    _channel: Any
    _hostname: Any
    _password: Any
    _port: Any
    _ssh: Any
    _term: Any
    _username: Any
    def __init__(self, hostname = ..., port = ..., username = ..., password = ..., term = ...) -> None: ...
    def _open(self) -> None: ...
    def close(self) -> Any: ...
    def recv(self, count = ...) -> Any: ...
    def resize(self, cols, rows) -> Any: ...
    def send(self, data) -> Any: ...
