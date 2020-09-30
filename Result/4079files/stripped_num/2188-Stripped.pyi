# (generated with --quick)

import http.server
import socketserver
from typing import Any, Iterable, NoReturn, Optional, Tuple, Type

DEFAULT_CAN_INTERFACE: str
HTTPRequestHandler: Any
HTTPServer: Type[http.server.HTTPServer]
HTTP_SERVER_IP_ADDRESS: str
HTTP_SERVER_PORT: int
ThreadingMixIn: Type[socketserver.ThreadingMixIn]
WebSocket: Any
server: ThreadedHTTPServer
signal: module
socketcan: Any
sys: module

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer): ...

class WebSocketCanHandler(Any):
    def listen(self) -> None: ...

def select(rlist: Iterable, wlist: Iterable, xlist: Iterable, timeout: Optional[float] = ...) -> Tuple[list, list, list]: ...
def sigterm_handler(signum, frame) -> NoReturn: ...
