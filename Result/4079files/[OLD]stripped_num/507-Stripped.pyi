# (generated with --quick)

from typing import Any, Optional, TextIO

DataReceived: Any
Deferred: Any
Factory: Any
H2Configuration: Any
H2Connection: Any
Protocol: Any
ProtocolError: Any
READ_CHUNK_SIZE: int
RequestReceived: Any
WindowUpdated: Any
cert: Any
cert_data: str
crypto: Any
endpoint: Any
endpoints: Any
f: TextIO
functools: module
inlineCallbacks: Any
key: Any
key_data: str
mimetypes: module
options: Any
os: module
reactor: Any
root: bytes
ssl: Any
sys: module

class H2Factory(Any):
    root: Any
    def __init__(self, root) -> None: ...
    def buildProtocol(self, addr) -> H2Protocol: ...

class H2Protocol(Any):
    _flow_control_deferreds: dict
    _send_file: Any
    conn: Any
    known_proto: Optional[bool]
    root: Any
    def __init__(self, root) -> None: ...
    def connectionMade(self) -> None: ...
    def dataFrameReceived(self, stream_id) -> None: ...
    def dataReceived(self, data) -> None: ...
    def requestReceived(self, headers, stream_id) -> None: ...
    def sendFile(self, file_path, stream_id) -> None: ...
    def wait_for_flow_control(self, stream_id) -> Any: ...
    def windowUpdated(self, event) -> None: ...

def close_file(file, d) -> None: ...
