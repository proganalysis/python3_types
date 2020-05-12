# (generated with --quick)

import http.server
from typing import Type

HOST_NAME: str
PORT_NUMBER: int
http: module
httpd: http.server.HTTPServer
os: module
server_class: Type[http.server.HTTPServer]
time: module

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(s: MyHandler) -> None: ...
