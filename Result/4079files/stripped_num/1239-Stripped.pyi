# (generated with --quick)

import http.server
from typing import Any, Generator

base64: module
http: module
os: module
pytest: Any
stub_auth_server: Any
stub_server: Any
threading: module

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_AUTHHEAD(self) -> None: ...

def _serve(request, handler) -> Generator[http.server.HTTPServer, Any, None]: ...
