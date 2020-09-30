# (generated with --quick)

import __future__
from typing import Any, Tuple, Type, TypeVar, Union

ALL: Tuple[str, str, str]
BokehDeprecationWarning: Any
BokehUserWarning: Any
Test___all__: Any
_LICENSE: str
absolute_import: __future__._Feature
b: Any
division: __future__._Feature
print_function: __future__._Feature
pytest: Any
string_types: Tuple[Type[str]]
unicode_literals: __future__._Feature
verify_all: Any
warnings: module

AnyStr = TypeVar('AnyStr', str, bytes)

class TestWarnings(object):
    test_bokeh_custom: Any
    def test_filters(self) -> None: ...
    def test_general_default(self) -> None: ...

def copy(src: Union[str, _PathLike[str]], dst: Union[str, _PathLike[str]], *, follow_symlinks: bool = ...) -> Any: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def test___version___defined() -> None: ...
def test___version___type() -> None: ...
def test_license(capsys) -> None: ...
