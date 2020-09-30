# (generated with --quick)

import functools
from typing import Any, Coroutine, Dict, List, Tuple, Type

CONNECTION_TIMEOUT: int
CRLF: bytes
DEFAULT_RECONNECT_INTERVAL: int
DEFAULT_SIGNAL_REPETITIONS: int
DELIM: Any
PacketHeader: Any
RflinkProtocol: Any
async_timeout: Any
asyncio: module
clients: List[Tuple[Any, Any, Any]]
create_serial_connection: Any
decode_packet: Any
docopt: Any
log: logging.Logger
logging: module
partial: Type[functools.partial]
pkg_resources: module
serialize_packet_id: Any
sys: module
valid_packet: Any

class ProxyProtocol(Any):
    __doc__: str
    _last_ack: Any
    def __init__(self, *args, raw_callback = ..., **kwargs) -> None: ...
    def handle_raw_packet(self, raw_packet) -> None: ...
    def raw_callback(self, _1) -> Any: ...

class RFLinkProxy:
    __doc__: str
    baud: Any
    closing: bool
    host: Any
    loop: Any
    port: Any
    protocol: Any
    transport: Any
    def __init__(self, port = ..., host = ..., baud = ..., loop = ...) -> None: ...
    def client_connected_callback(self, reader, writer) -> Coroutine[Any, Any, None]: ...
    def connect(self) -> Coroutine[Any, Any, None]: ...
    def forward_packet(self, writer, packet, raw_packet) -> Coroutine[Any, Any, None]: ...
    def handle_raw_tx_packet(self, writer, raw_packet) -> Coroutine[Any, Any, None]: ...
    def raw_callback(self, raw_packet) -> None: ...
    def reconnect(self, exc = ...) -> None: ...

def decode_tx_packet(packet) -> Dict[str, Any]: ...
def main(argv = ..., loop = ...) -> None: ...
