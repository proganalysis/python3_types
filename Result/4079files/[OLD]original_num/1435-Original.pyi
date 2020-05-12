# (generated with --quick)

import __future__
from typing import Any, List, Optional, Tuple, TypeVar, Union

Cython: Any
Extension: Any
absolute_import: __future__._Feature
build_ext: Any
find_packages: Any
io: module
os: module
print_function: __future__._Feature
re: module
setup: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class optional_build_ext(Any):
    __doc__: str
    extensions: List[nothing]
    def _unavailable(self, e) -> None: ...
    def run(self) -> None: ...

def basename(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def read(*names, **kwargs) -> Union[bytes, str]: ...
@overload
def relpath(path: Union[bytes, _PathLike[bytes]], start: Optional[Union[bytes, _PathLike[bytes]]] = ...) -> bytes: ...
@overload
def relpath(path: Union[str, _PathLike[str]], start: Optional[Union[str, _PathLike[str]]] = ...) -> str: ...
def splitext(path: Union[_PathLike[AnyStr], AnyStr]) -> Tuple[AnyStr, AnyStr]: ...
