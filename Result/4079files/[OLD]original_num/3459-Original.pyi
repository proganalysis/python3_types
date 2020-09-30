# (generated with --quick)

import enum
from typing import Any, Type

Enum: Type[enum.Enum]

class Color(enum.Enum):
    BLACK: str
    BLUE: str
    GREEN: str
    ORANGE: str
    PURPLE: str
    RED: str
    SQUARE: str
    TURQUOISE: str
    WHITE: str
    def Darker(color: Color, blackRatio = ...) -> Any: ...
    def FromRGB(r: Color, g, b) -> str: ...
    def Lighter(color: Color, whiteRatio = ...) -> Any: ...
    def Mix(color1: Color, color2, ratio = ...) -> Any: ...
