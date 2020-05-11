# (generated with --quick)

from typing import Any, Pattern, Tuple

ExecutorType: Any
TCPExecutor: Any
os: module
re: module
shutil: module
subprocess: module
time: module

class PostgreSQLExecutor(Any):
    BASE_PROC_START_COMMAND: str
    MIN_SUPPORTED_VERSION: Tuple[str, ...]
    VERSION_RE: Pattern[str]
    __doc__: str
    _directory_initialised: bool
    datadir: Any
    executable: Any
    logfile: Any
    options: Any
    startparams: Any
    unixsocketdir: Any
    user: Any
    version: Tuple[str, ...]
    def __del__(self) -> None: ...
    def __init__(self, executable, host, port, datadir, unixsocketdir, logfile, startparams, shell = ..., timeout = ..., sleep = ..., user = ..., options = ...) -> None: ...
    def clean_directory(self) -> None: ...
    def init_directory(self) -> None: ...
    def proc_start_command(self) -> str: ...
    def running(self) -> bool: ...
    def start(self) -> Any: ...
    def stop(self, sig = ...) -> None: ...
    def wait_for_postgres(self) -> None: ...

class PostgreSQLUnsupported(Exception):
    __doc__: str

def parse_version(v: str) -> Tuple[str, ...]: ...
