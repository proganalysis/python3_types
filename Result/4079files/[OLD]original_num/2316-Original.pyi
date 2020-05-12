# (generated with --quick)

from typing import Any, Tuple

Packet: Any

class CLIENT_HANDSHAKE_DataPacket(Any):
    PID: int
    address: Any
    port: Any
    sendPing: Any
    sendPong: Any
    systemAddresses: Tuple[nothing, ...]
    def _decode(self) -> None: ...
    def _encode(self) -> None: ...
