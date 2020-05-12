from typing import Any, Optional

_LOGGER: Any

class PatchedDTLSSecurityStore:
    IDENTITY: Any = ...
    KEY: Any = ...
    def _get_psk(self, host: Any, port: Any): ...

class APIFactory:
    _psk: Any = ...
    _host: Any = ...
    _psk_id: Any = ...
    _loop: Any = ...
    _observations_err_callbacks: Any = ...
    _protocol: Any = ...
    def __init__(self, host: Any, psk_id: str = ..., psk: Optional[Any] = ..., loop: Optional[Any] = ...) -> None: ...
    @property
    def psk_id(self): ...
    @psk_id.setter
    def psk_id(self, value: Any) -> None: ...
    @property
    def psk(self): ...
    @psk.setter
    def psk(self, value: Any) -> None: ...
    async def _get_protocol(self): ...
    async def _reset_protocol(self, exc: Optional[Any] = ...) -> None: ...
    async def shutdown(self, exc: Optional[Any] = ...) -> None: ...
    async def _get_response(self, msg: Any): ...
    async def _execute(self, api_command: Any): ...
    async def request(self, api_commands: Any): ...
    async def _observe(self, api_command: Any) -> None: ...
    async def generate_psk(self, security_key: Any): ...

def _process_output(res: Any, parse_json: bool = ...): ...
