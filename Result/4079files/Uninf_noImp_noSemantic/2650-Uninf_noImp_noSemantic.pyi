from http.server import SimpleHTTPRequestHandler
from typing import Any

ROUTE_MAP: Any

class InfoPiRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self): ...
