# (generated with --quick)

from typing import Any, Tuple, TypeVar

Image: module
np: module
piexif: Any

_T1 = TypeVar('_T1')

def append_postfix(filename, postfix) -> str: ...
def imread(filepath) -> Tuple[Any, Any]: ...
def imwrite(image, filename, exif = ...) -> None: ...
def try_rot_exif(image, exf: _T1) -> Tuple[bool, Any, _T1]: ...
