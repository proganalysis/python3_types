# (generated with --quick)

from typing import Any, Dict

capi: Any

class Client:
    NONE: int
    STD: int
    TCPV4: int
    TCPV6: int
    UDPV4: int
    UDPV6: int
    _TYPE_NAME_MAP: Dict[int, str]
    __doc__: str
    _name: Any
    _port: Any
    _skull_txn: Any
    _type: Any
    def _Client__setup_peer_info(self) -> None: ...
    def __init__(self, skull_txn) -> None: ...
    def name(self) -> Any: ...
    def port(self) -> Any: ...
    def type(self) -> Any: ...
    def typeName(self) -> str: ...
