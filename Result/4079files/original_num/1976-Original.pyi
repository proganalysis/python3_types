# (generated with --quick)

from typing import Any

class SNMPError(Exception):
    __doc__: str

class SNMPInvalidAddress(SNMPError):
    __doc__: str
    host: Any
    message: str
    def __init__(self, host) -> None: ...

class SNMPTableError(SNMPError):
    __doc__: str
    message: str
    oid: Any
    def __init__(self, oid) -> None: ...

class SNMPTimeout(SNMPError):
    IP: Any
    __doc__: str
    message: str
    def __init__(self, ip) -> None: ...

class SNMPWriteError(SNMPError):
    __doc__: str
