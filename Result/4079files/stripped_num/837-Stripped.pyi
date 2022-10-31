# (generated with --quick)

from typing import Any, List, Tuple, TypeVar

os: module
shutil: module
sys: module
zipfile: module

_TTextReplacer = TypeVar('_TTextReplacer', bound=TextReplacer)

class TextReplacer:
    res: List[Tuple[Any, Any]]
    def __init__(self) -> None: ...
    def add(self: _TTextReplacer, reg, rep) -> _TTextReplacer: ...
    def replace(self, text) -> Any: ...

def appveyor_msbuild() -> str: ...
def dir_exist(path) -> bool: ...
def download_file(url, path) -> None: ...
def extract_zip(proto_zip, proto_root) -> None: ...
def flush() -> None: ...
def globals() -> None: ...
def is_platform_64bit() -> bool: ...
def is_windows() -> bool: ...
def movefiles(from_directory, to_directory) -> None: ...
def print_dashes() -> None: ...
def print_file(path) -> None: ...
def print_files_and_folders(root, start = ...) -> None: ...
def rename_file(from_path, to_path) -> None: ...
def verify_dir_exist(path) -> None: ...