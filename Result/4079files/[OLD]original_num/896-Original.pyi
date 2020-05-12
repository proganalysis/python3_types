# (generated with --quick)

from typing import Any, Optional

client_s: Any
listen_s: Optional[socket.socket]
network: Any
socket: module
uos: Any
websocket: Any
websocket_helper: Any

def accept_conn(listen_sock) -> None: ...
def setup_conn(port, accept_handler) -> socket.socket: ...
def start(port = ..., password = ...) -> None: ...
def start_foreground(port = ...) -> None: ...
def stop() -> None: ...
