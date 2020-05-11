# (generated with --quick)

from typing import TypeVar, Union

setuptools: module

AnyStr = TypeVar('AnyStr', str, bytes)

def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def read(fname) -> str: ...
