# (generated with --quick)

import http.client
import io
from typing import Any, Callable, Optional, Type

BytesIO: Type[io.BytesIO]
TTransportBase: Any
http_client: module
os: module
six: module
socket: module
sys: module
urllib: module
warnings: module

class THttpClient(Any):
    _THttpClient__custom_headers: Any
    _THttpClient__http: Optional[http.client.HTTPConnection]
    _THttpClient__http_response: None
    _THttpClient__timeout: Any
    _THttpClient__wbuf: io.BytesIO
    __doc__: str
    host: Any
    path: Any
    port: Any
    scheme: Any
    def _THttpClient__withTimeout(f: THttpClient) -> Callable: ...
    def __init__(self, uri_or_host, port = ..., path = ...) -> None: ...
    def close(self) -> None: ...
    def flush(*args, **kwargs) -> None: ...
    def isOpen(self) -> bool: ...
    def open(self) -> None: ...
    def read(self, sz) -> Any: ...
    def setCustomHeaders(self, headers) -> None: ...
    def setTimeout(self, ms) -> None: ...
    def write(self, buf) -> None: ...
