# (generated with --quick)

import io
import pathlib
from typing import Any, List, Tuple, Type

BytesIO: Type[io.BytesIO]
Path: Type[pathlib.Path]
docker: Any
tarfile: module

class Sandbox:
    container: Any
    docker_client: Any
    host_config: Any
    def __del__(self) -> None: ...
    def __init__(self, host_port = ...) -> None: ...
    def copy_file_to_sandbox(self, file_path: str, dest_path: str) -> bool: ...
    def `exec`(self, cmd: str) -> dict: ...
    def get_files_from_sandbox(self, file_path: str) -> List[Tuple[str, bytes]]: ...
    def write_files_in_sandbox(self, files: List[Tuple[str, bytes]], dest_dir: str) -> bool: ...
