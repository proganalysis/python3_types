# (generated with --quick)

import pathlib
from typing import Any, Optional, Tuple, Type

Path: Type[pathlib.Path]
_SortImports: Any
ask_whether_to_apply_changes_to_file: Any
locale: module
os: module
re: module
settings: module
show_unified_diff: Any
sys: module

class SortImports(object):
    config: Any
    file_path: Optional[pathlib.Path]
    incorrectly_sorted: bool
    length_change: int
    output: Any
    sections: Any
    skipped: bool
    sorted_imports: Any
    def __init__(self, file_path: Optional[str] = ..., file_contents: Optional[str] = ..., write_to_stdout: bool = ..., check: bool = ..., show_diff: bool = ..., settings_path: Optional[str] = ..., ask_to_apply: bool = ..., run_path: str = ..., check_skip: bool = ..., extension: Optional[str] = ..., **setting_overrides) -> None: ...

def determine_file_encoding(file_path: pathlib.Path, default: str = ...) -> str: ...
def get_settings_path(settings_path: Optional[pathlib.Path], current_file_path: Optional[pathlib.Path]) -> pathlib.Path: ...
def read_file_contents(file_path: pathlib.Path, encoding: str, fallback_encoding: str) -> Tuple[Optional[str], Optional[str]]: ...
def resolve(path: pathlib.Path) -> pathlib.Path: ...
