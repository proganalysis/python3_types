# (generated with --quick)

import __future__
import enum
from typing import Any, Optional, Tuple, Type

Builder: Any
CoreImage: Any
Enum: Type[enum.Enum]
Image: Any
ObjectProperty: Any
division: __future__._Feature
io: module
os: module

class Slide(Any):
    height: Any
    is_loaded: bool
    load_mode: Any
    mode: Any
    size: Any
    size_hint: Tuple[Optional[int], Optional[int]]
    texture: Any
    width: Any
    zoom: Any
    def __init__(self, session = ..., load_mode = ..., cursor = ..., **kwargs) -> None: ...
    def on_height(self, obj, value) -> None: ...
    def on_image_loaded(self, *args) -> None: ...
    def on_mode(self, obj, value) -> None: ...
    def on_texture_size(self, instance, value) -> None: ...
    def on_width(self, obj, value) -> None: ...
    def reset_zoom(self) -> None: ...

class SlideMode(enum.Enum):
    FIT_HEIGHT: int
    FIT_SCREEN: int
    FIT_WIDTH: int
    NORMAL: int
