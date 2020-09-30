# (generated with --quick)

import asyncio.tasks
from typing import Any, Coroutine, Optional, Tuple

ClientError: Any
Code: Any
ConstructionRenderableError: Any
Context: Any
Error: Any
Gateway: Any
Message: Any
RequestTimedOut: Any
RequestTimeout: Any
ServerError: Any
_LOGGER: logging.Logger
asyncio: module
json: module
logging: module
socket: module
tinydtls: Any

class APIFactory:
    _host: Any
    _loop: Any
    _observations_err_callbacks: list
    _protocol: Optional[asyncio.tasks.Task[nothing]]
    _psk: Any
    _psk_id: Any
    psk: Any
    psk_id: Any
    def __init__(self, host, psk_id = ..., psk = ..., loop = ...) -> None: ...
    def _execute(self, api_command) -> coroutine: ...
    def _get_protocol(self) -> coroutine: ...
    def _get_response(self, msg) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def _observe(self, api_command) -> Coroutine[Any, Any, None]: ...
    def _reset_protocol(self, exc = ...) -> Coroutine[Any, Any, None]: ...
    def generate_psk(self, security_key) -> coroutine: ...
    def request(self, api_commands) -> coroutine: ...
    def shutdown(self, exc = ...) -> Coroutine[Any, Any, None]: ...

class PatchedDTLSSecurityStore:
    IDENTITY: Any
    KEY: Any
    __doc__: str
    def _get_psk(self, host, port) -> Tuple[Any, Any]: ...

def _process_output(res, parse_json = ...) -> Any: ...
