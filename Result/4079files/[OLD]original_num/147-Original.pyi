# (generated with --quick)

import io
from typing import Any, Dict, List, Optional, Type, TypeVar

FileIO: Type[io.FileIO]
SANDBOX_DOCKER_IMAGE: str
SANDBOX_HOME_DIR_NAME: str
SANDBOX_USERNAME: str
SANDBOX_WORKING_DIR_NAME: str
VERSION: str
_NEXT_UID_KEY: str
_REDIS_SETTINGS: Dict[str, str]
json: module
os: module
redis: module
subprocess: module
tarfile: module
tempfile: module
uuid: module

_TAutograderSandbox = TypeVar('_TAutograderSandbox', bound=AutograderSandbox)

class AutograderSandbox:
    __doc__: str
    _allow_network_access: bool
    _container_create_timeout: Optional[int]
    _docker_image: str
    _environment_variables: Optional[dict]
    _is_running: bool
    _linux_uid: Any
    _name: str
    allow_network_access: bool
    debug: Any
    docker_image: str
    environment_variables: dict
    name: str
    def __enter__(self: _TAutograderSandbox) -> _TAutograderSandbox: ...
    def __exit__(self, *args) -> None: ...
    def __init__(self, name: Optional[str] = ..., docker_image: str = ..., allow_network_access: bool = ..., environment_variables: Optional[dict] = ..., container_create_timeout: Optional[int] = ..., debug = ...) -> None: ...
    def _chown_files(self, filenames) -> None: ...
    def _create_and_start(self) -> None: ...
    def _destroy(self) -> None: ...
    def _stop(self) -> None: ...
    def add_and_rename_file(self, filename: str, new_filename: str) -> None: ...
    def add_files(self, *filenames: str, owner: str = ..., read_only: bool = ...) -> None: ...
    def reset(self) -> None: ...
    def restart(self) -> None: ...
    def run_command(self, args: List[str], max_num_processes: Optional[int] = ..., max_stack_size: Optional[int] = ..., max_virtual_memory: Optional[int] = ..., as_root: bool = ..., stdin: Optional[io.FileIO] = ..., timeout: Optional[int] = ..., check: bool = ..., truncate_stdout: Optional[int] = ..., truncate_stderr: Optional[int] = ...) -> CompletedCommand: ...

class CompletedCommand:
    return_code: int
    stderr: io.FileIO
    stderr_truncated: bool
    stdout: io.FileIO
    stdout_truncated: bool
    timed_out: bool
    def __init__(self, return_code: int, stdout: io.FileIO, stderr: io.FileIO, timed_out: bool, stdout_truncated: bool, stderr_truncated: bool) -> None: ...

def _get_next_linux_uid() -> Any: ...
