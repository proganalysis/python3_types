from http.server import HTTPServer
from socketserver import ThreadingMixIn
from typing import Any
from websocket import HTTPRequestHandler

DEFAULT_CAN_INTERFACE: str
HTTP_SERVER_IP_ADDRESS: str
HTTP_SERVER_PORT: int

def sigterm_handler(signum: Any, frame: Any) -> None: ...

class WebSocketCanHandler(HTTPRequestHandler):
    def listen(self) -> None: ...

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer): ...

server: Any
