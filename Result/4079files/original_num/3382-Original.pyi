# (generated with --quick)

from typing import Any, IO, Optional, Type, TypeVar, Union
import unittest.case

FileAttributeManager: Any
TestCase: Type[unittest.case.TestCase]
h5py: Any
np: module
os: module

AnyStr = TypeVar('AnyStr', str, bytes)

class FileAttributeManagerTests(unittest.case.TestCase):
    VALUE_IN_FILE: Any
    file: Any
    filename: str
    def test_get(self) -> None: ...

@overload
def NamedTemporaryFile(mode, buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[str]: ...
@overload
def NamedTemporaryFile(mode = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[bytes]: ...
@overload
def NamedTemporaryFile(mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO: ...
