# (generated with --quick)

from typing import Any, Optional, TypeVar, Union

BaseUnitTestCase: Any
os: module

AnyStr = TypeVar('AnyStr', str, bytes)

class TestTest(Any):
    __doc__: str
    def test_all_test_subdirectories_have_init_py_file(self) -> None: ...

def basename(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
@overload
def relpath(path: Union[bytes, _PathLike[bytes]], start: Optional[Union[bytes, _PathLike[bytes]]] = ...) -> bytes: ...
@overload
def relpath(path: Union[str, _PathLike[str]], start: Optional[Union[str, _PathLike[str]]] = ...) -> str: ...
