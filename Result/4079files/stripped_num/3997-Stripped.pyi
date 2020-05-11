# (generated with --quick)

import io
import pathlib
from typing import Any, Dict, List, Tuple, Type

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
    def copy_file_to_sandbox(self, file_path, dest_path) -> Any: ...
    def `exec`(self, cmd) -> Dict[str, Any]: ...
    def get_files_from_sandbox(self, file_path) -> List[Tuple[str, bytes]]: ...
    def write_files_in_sandbox(self, files, dest_dir) -> Any: ...
