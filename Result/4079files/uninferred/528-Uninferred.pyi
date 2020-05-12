import http.server
from typing import Any

HOST_NAME: str
PORT_NUMBER: Any

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(s: Any) -> None: ...
