# (generated with --quick)

import io
from typing import Any, Dict, Type, TypeVar

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
    _allow_network_access: Any
    _container_create_timeout: Any
    _docker_image: Any
    _environment_variables: Any
    _is_running: bool
    _linux_uid: Any
    _name: Any
    allow_network_access: Any
    debug: Any
    docker_image: Any
    environment_variables: dict
    name: Any
    def __enter__(self: _TAutograderSandbox) -> _TAutograderSandbox: ...
    def __exit__(self, *args) -> None: ...
    def __init__(self, name = ..., docker_image = ..., allow_network_access = ..., environment_variables = ..., container_create_timeout = ..., debug = ...) -> None: ...
    def _chown_files(self, filenames) -> None: ...
    def _create_and_start(self) -> None: ...
    def _destroy(self) -> None: ...
    def _stop(self) -> None: ...
    def add_and_rename_file(self, filename, new_filename) -> None: ...
    def add_files(self, *filenames, owner = ..., read_only = ...) -> None: ...
    def reset(self) -> None: ...
    def restart(self) -> None: ...
    def run_command(self, args, max_num_processes = ..., max_stack_size = ..., max_virtual_memory = ..., as_root = ..., stdin = ..., timeout = ..., check = ..., truncate_stdout = ..., truncate_stderr = ...) -> CompletedCommand: ...

class CompletedCommand:
    return_code: Any
    stderr: Any
    stderr_truncated: Any
    stdout: Any
    stdout_truncated: Any
    timed_out: Any
    def __init__(self, return_code, stdout, stderr, timed_out, stdout_truncated, stderr_truncated) -> None: ...

def _get_next_linux_uid() -> Any: ...
