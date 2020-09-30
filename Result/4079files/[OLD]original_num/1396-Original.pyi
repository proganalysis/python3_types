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
clean_version: str
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
version_val: Any
warning_banner: str
warning_version_mismatch: str

AnyStr = TypeVar('AnyStr', str, bytes)

class FileVersionInfo(object):
    file_path: str
    key_name: str
    magic_line: str
    strip_end_chars: int
    def __init__(self, key_name: str, file_path: str, magic_line: str, strip_end_chars: int = ...) -> None: ...
    def get_version(self) -> str: ...
    def set_version(self, new_version: str) -> None: ...

class FileVersionResult(object):
    uniform: bool
    version_details: dict
    version_result: str
    def __init__(self, uniform: bool, version_details: dict, version_result: str) -> None: ...

def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def get_version_with_beta(version_info: FileVersionResult) -> str: ...
def get_version_without_beta(version_info: FileVersionResult) -> str: ...
def get_versions() -> FileVersionResult: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def set_versions(new_version: str) -> None: ...
