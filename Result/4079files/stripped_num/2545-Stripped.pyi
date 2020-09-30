# (generated with --quick)

import pathlib
from typing import Any, Optional, Tuple, Type, TypeVar

Path: Type[pathlib.Path]
_SortImports: Any
ask_whether_to_apply_changes_to_file: Any
locale: module
os: module
re: module
settings: module
show_unified_diff: Any
sys: module

_T1 = TypeVar('_T1')

class SortImports(object):
    config: Any
    file_path: Optional[pathlib.Path]
    incorrectly_sorted: bool
    length_change: Any
    output: Any
    sections: Any
    skipped: bool
    sorted_imports: Any
    def __init__(self, file_path = ..., file_contents = ..., write_to_stdout = ..., check = ..., show_diff = ..., settings_path = ..., ask_to_apply = ..., run_path = ..., check_skip = ..., extension = ..., **setting_overrides) -> None: ...

def determine_file_encoding(file_path, default = ...) -> Any: ...
def get_settings_path(settings_path, current_file_path) -> Any: ...
def read_file_contents(file_path, encoding: _T1, fallback_encoding) -> Tuple[Any, _T1]: ...
def resolve(path) -> Any: ...
