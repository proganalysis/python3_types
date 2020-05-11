# (generated with --quick)

from typing import Any, List

Packet: Any

class SERVER_HANDSHAKE_DataPacket(Any):
    PID: int
    address: Any
    port: Any
    sendPing: Any
    sendPong: Any
    systemAddresses: List[list]
    def _decode(self) -> None: ...
    def _encode(self) -> None: ...
