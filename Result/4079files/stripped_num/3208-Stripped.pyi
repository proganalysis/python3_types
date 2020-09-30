# (generated with --quick)

from typing import Union

os: module
subprocess: module
sys: module

def go() -> None: ...
@overload
def path(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def path(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
