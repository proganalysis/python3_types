# (generated with --quick)

import hashlib
from typing import Any, Union

BORDER_SIZE: int
GRID_SIZE: int
Image: module
ImageDraw: module
SQUARE_SIZE: int

class Identicon(object):
    draw: Any
    hash: int
    image: Any
    name: Any
    def __init__(self, str_, background = ...) -> None: ...
    def calculate(self) -> None: ...
    def digest(self, str_) -> int: ...
    def generate(self) -> None: ...

def md5(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
