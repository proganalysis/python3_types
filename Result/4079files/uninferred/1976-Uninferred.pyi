from typing import Any

class SNMPError(Exception): ...

class SNMPTableError(SNMPError):
    oid: Any = ...
    message: Any = ...
    def __init__(self, oid: Any) -> None: ...

class SNMPTimeout(SNMPError):
    IP: Any = ...
    message: Any = ...
    def __init__(self, ip: Any) -> None: ...

class SNMPInvalidAddress(SNMPError):
    host: Any = ...
    message: Any = ...
    def __init__(self, host: Any) -> None: ...

class SNMPWriteError(SNMPError): ...
