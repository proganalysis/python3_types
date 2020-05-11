# (generated with --quick)

from typing import Any, Dict, List

math: module

class CompositeElement(object):
    __doc__: str
    elements: List[nothing]
    def initialize(self, canvas) -> None: ...
    def move(self, v) -> None: ...
    def rotate(self, angle) -> None: ...
    def update_coordinates(self) -> None: ...

class DrawableElement(object):
    __doc__: str
    angle: Any
    canvas: Any
    center: Any
    color: Any
    flat_pts: list
    id: Any
    pts: Any
    def __init__(self, pts, center, angle, color) -> None: ...
    def delete(self) -> None: ...
    def initialize(self, canvas) -> None: ...
    def intersects(self) -> None: ...
    def move(self, v) -> None: ...
    def perform_move(self) -> None: ...
    def rotate(self, angle) -> None: ...
    def set_color(self, color) -> None: ...
    def update_coordinates(self) -> None: ...

class DrawableLine(DrawableElement):
    __doc__: str
    angle: int
    canvas: Any
    center: Any
    color: Any
    id: Any
    pts: Any
    tkargs: Any
    def __init__(self, pts, color, tkargs) -> None: ...

class TextElement(DrawableElement):
    __doc__: str
    angle: Any
    canvas: Any
    center: Any
    color: Any
    fontSize: Any
    id: Any
    pts: list
    text: Any
    tkargs: Dict[str, Any]
    def __init__(self, text, center, angle, color, fontSize, **kwargs) -> None: ...
