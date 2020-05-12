# (generated with --quick)

import typing
from typing import Any, List, Type, TypeVar

Circle: Any
Element: Any
ElementTree: module
Elements: Any
HALF_PI: Any
Line: Any
Path: Any
Point: Any
Polygon: Any
Polyline: Any
Rect: Any
Sequence: Type[typing.Sequence]
__all__: List[str]
elements: Any

_TSVG = TypeVar('_TSVG', bound=SVG)

class SVG:
    __doc__: str
    _height: Any
    _invert_y: Any
    _offset: Any
    _root: Any
    def __init__(self, width = ..., height = ..., background = ..., attributes = ..., root = ..., offset = ..., invert_y = ...) -> None: ...
    def add(self, element) -> None: ...
    def add_raw(self, tag, attributes, text = ...) -> None: ...
    def circle(self, center, radius, **attributes) -> None: ...
    def export(self) -> bytes: ...
    @classmethod
    def format(cls, value) -> Any: ...
    @classmethod
    def format_attributes(cls, attributes) -> dict: ...
    def line(self, start, end, **attributes) -> None: ...
    def offset(self: _TSVG, point) -> _TSVG: ...
    def path(self, *descriptions, **attributes) -> None: ...
    def polygon(self, points, **attributes) -> None: ...
    def polyline(self, points, **attributes) -> None: ...
    def rect(self, top_left, width, height = ..., **attributes) -> None: ...
    def rectangle(self, top_left, bottom_right, **attributes) -> None: ...
    def star(self, center, length, num_points, rotation = ..., ngram = ..., inner_length = ..., **attributes) -> None: ...
