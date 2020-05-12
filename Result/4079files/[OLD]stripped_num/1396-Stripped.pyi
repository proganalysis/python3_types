# (generated with --quick)

import argparse
import collections
import typing
from typing import Any, List, Type, TypeVar, Union

ArgumentParser: Type[argparse.ArgumentParser]
Counter: Type[typing.Counter]
OrderedDict: Type[collections.OrderedDict]
args: argparse.Namespace
build_version: str
clean_version: Any
command: str
curr_location: str
datetime: module
key: Any
new_version_str: str
parser: argparse.ArgumentParser
sp: argparse._SubParsersAction
sys: module
understood_commands: List[str]
version_data: FileVersionResult
version_objects: List[FileVersionInfo]
version_val: str
warning_banner: str
warning_version_mismatch: str

AnyStr = TypeVar('AnyStr', str, bytes)

class FileVersionInfo(object):
    file_path: Any
    key_name: Any
    magic_line: Any
    strip_end_chars: Any
    def __init__(self, key_name, file_path, magic_line, strip_end_chars = ...) -> None: ...
    def get_version(self) -> str: ...
    def set_version(self, new_version) -> None: ...

class FileVersionResult(object):
    uniform: Any
    version_details: Any
    version_result: Any
    def __init__(self, uniform, version_details, version_result) -> None: ...

def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def get_version_with_beta(version_info) -> str: ...
def get_version_without_beta(version_info) -> Any: ...
def get_versions() -> FileVersionResult: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def set_versions(new_version) -> None: ...
