# (generated with --quick)

import __future__
from typing import Any, BinaryIO, Optional

AUTHORITY: str
DataReceived: Any
H2Connection: Any
PATH: str
Protocol: Any
ResponseReceived: Any
SSL4ClientEndpoint: Any
SettingsAcknowledged: Any
StreamEnded: Any
StreamReset: Any
WindowUpdated: Any
connectProtocol: Any
defer: Any
filename: str
mimetypes: module
options: Any
optionsForClientTLS: Any
os: module
print_function: __future__._Feature
reactor: Any
sys: module

class H2Protocol(Any):
    conn: Any
    file_path: Any
    file_size: Any
    fileobj: Optional[BinaryIO]
    flow_control_deferred: Any
    known_proto: Any
    request_complete: bool
    request_made: bool
    def __init__(self, file_path) -> None: ...
    def connectionLost(self, reason = ...) -> None: ...
    def connectionMade(self) -> None: ...
    def dataReceived(self, data) -> None: ...
    def endStream(self) -> None: ...
    def handleData(self, data) -> None: ...
    def handleResponse(self, response_headers) -> None: ...
    def sendFileData(self) -> None: ...
    def sendRequest(self) -> None: ...
    def settingsAcked(self, event) -> None: ...
    def windowUpdated(self, event) -> None: ...
