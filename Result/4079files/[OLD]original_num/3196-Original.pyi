# (generated with --quick)

import asyncio.futures
from typing import Any, Coroutine

NameOID: Any
asyncio: module
datetime: module
hashes: Any
hashlib: module
logger: Any
os: module
rsa: Any
serialization: module
x509: module

class Certificate:
    _name: str
    app: Any
    public_cert_bytes_result: asyncio.futures.Future[nothing]
    server_cert_path: str
    server_key_path: str
    def __init__(self, app) -> None: ...
    def digest(self) -> Coroutine[Any, Any, bytes]: ...
    def public_cert_bytes(self) -> Coroutine[Any, Any, nothing]: ...
    def start(self) -> Coroutine[Any, Any, None]: ...
    def stop(self) -> Coroutine[Any, Any, None]: ...

def default_backend() -> Any: ...
