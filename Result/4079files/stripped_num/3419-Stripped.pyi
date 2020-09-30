# (generated with --quick)

from typing import Any, NoReturn, Union

TftpErrors: Any
TftpException: Any
TftpPacketRRQ: Any
TftpPacketWRQ: Any
TftpStateExpectACK: Any
TftpStateExpectDAT: Any
errors: Any
fs: Any
logger: logging.Logger
logging: module
monkey: Any
os: module
sanitize_file_name: Any
socket: Any
tftpy: Any
time: module

class TFTPContextServer(Any):
    __doc__: str
    _already_uploaded: bool
    data_fs: None
    data_fs_fileobj: None
    file_path: None
    last_update: float
    log: logging.Logger
    root: Any
    sock: Any
    state: Any
    vfs: None
    def __int__(self, host, port, timeout, root, dyn_file_func, upload_open) -> None: ...
    def end(self) -> None: ...
    def start(self, buffer) -> None: ...

class TFTPServerState(TFTPState):
    __doc__: str
    data_fs: None
    full_path: Any
    vfs: None
    def serverInitial(self, pkt, raddress, rport) -> Union[TFTPServerState, bool]: ...

class TFTPState(Any):
    def __int__(self, context) -> None: ...
    def handle(self, pkt, raddress, rport) -> NoReturn: ...

class TFTPStateServerRecvRRQ(TFTPServerState):
    full_path: Any
    def handle(self, pkt, raddress, rport) -> Any: ...

class TFTPStateServerRecvWRQ(TFTPServerState):
    __doc__: str
    full_path: Any
    def handle(self, pkt, raddress, rport) -> Any: ...
    def make_subdirs(self) -> None: ...

class TFTPStateServerStart(TFTPState):
    __doc__: str
    log: logging.Logger
    def handle(self, pkt, raddress, rport) -> Any: ...
