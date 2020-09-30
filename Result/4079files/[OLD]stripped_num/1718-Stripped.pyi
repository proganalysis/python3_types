# (generated with --quick)

import typing
from typing import Any, TextIO, Tuple, Type

Iterable: Type[typing.Iterable]
_Error: Any
anyconfig: Any
find_project_dir: Any
get_file: Any
path: module
stderr: TextIO

class Config:
    __doc__: str
    config_file: Any
    config_files: list
    error: str
    project_dir: Any
    spec_files: list
    def __init__(self, config_file) -> None: ...
    def _build_config_files_list(self) -> None: ...
    def _build_config_schemas_list(self) -> None: ...
    def display_errors(self) -> None: ...
    def read(self) -> Any: ...

def get_config_and_project_dir(config_file) -> Tuple[Any, Any]: ...
