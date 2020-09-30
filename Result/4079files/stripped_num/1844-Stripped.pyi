# (generated with --quick)

from typing import Any, IO, List, Optional, TypeVar, Union
import unittest.case

LOCAL_DIR: str
conftest: Any
filecmp: module
gb_reader_b: Any
gb_writer_b: Any
json: module
os: module
unittest: module

AnyStr = TypeVar('AnyStr', str, bytes)

class TestGBWriter(unittest.case.TestCase):
    bad_files: List[str]
    good_files: List[str]
    maxDiff: None
    def checkFile(self, fn, should_be_true) -> None: ...
    def test_badFiles(self) -> None: ...
    def test_goodFiles(self) -> None: ...

@overload
def NamedTemporaryFile(mode, buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[str]: ...
@overload
def NamedTemporaryFile(mode = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[bytes]: ...
@overload
def NamedTemporaryFile(mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO: ...
def abspath(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
