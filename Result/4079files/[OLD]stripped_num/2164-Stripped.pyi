# (generated with --quick)

import __builtin__
import client
from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Type, Union

AUTOGENTOO_ACCESS_TOKEN: int
AUTOGENTOO_FILE_END: int
AUTOGENTOO_HOST: int
AUTOGENTOO_HOST_END: int
AUTOGENTOO_SERVER_TOKEN: int
AUTOGENTOO_SUDO_TOKEN: int
BinaryFileReader: Any
Host: Type[client.Host]
Server: Type[client.Server]
Token: Type[client.Token]
WORKER_FIFO_REQUEST: str
WORKER_FIFO_RESPONSE: str
_thread: module
importlib: module
logfp: Optional[TextIO]
os: module
struct: module
sys: module
traceback: module

class Job:
    args: Any
    command_name: Any
    host: Any
    job_name: Any
    module: __builtin__.module
    pid: int
    res: int
    server: Any
    def __init__(self, server, host, job_name, command_name, args) -> None: ...
    def join(self) -> None: ...
    def run(self) -> int: ...

class Worker:
    jobs: List[Job]
    keep_alive: bool
    pid: Optional[int]
    read_lck: Optional[_thread.LockType]
    request_fifo: Optional[BinaryIO]
    response_fifo: Optional[BinaryIO]
    running_jobs: Dict[nothing, nothing]
    server: Any
    write_lck: Optional[_thread.LockType]
    def __init__(self, server) -> None: ...
    def close(self) -> None: ...
    def read_int(self) -> Any: ...
    def read_str(self) -> Optional[str]: ...
    def start(self) -> Any: ...
    def write_int(self, i) -> None: ...
    def write_str(self, string) -> None: ...

def cd(path: Union[_PathLike, bytes, int, str]) -> None: ...
def main(argv) -> None: ...
def mkdir(path) -> None: ...
def rm(path: Union[_PathLike, bytes, str], *, dir_fd: Optional[int] = ...) -> None: ...
def touch(filepath) -> None: ...
