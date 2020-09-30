# (generated with --quick)

import enum
from typing import Any, Type, TypeVar

Enum: Type[enum.Enum]
colorama: Any

_EnumType = TypeVar('_EnumType', bound=Type[enum.Enum])

class Color(enum.Enum):
    black: int
    blue: int
    cyan: int
    green: int
    light_black: int
    light_blue: int
    light_cyan: int
    light_green: int
    light_magenta: int
    light_red: int
    light_white: int
    light_yellow: int
    magenta: int
    red: int
    white: int
    yellow: int

def cprint(color, mess, **kwargs) -> None: ...
def print_error(mess, **kwargs) -> None: ...
def print_good(mess, **kwargs) -> None: ...
def print_info(mess, **kwargs) -> None: ...
def print_pair(a, b, width = ...) -> None: ...
def print_text(mess, **kwargs) -> None: ...
def print_warn(mess, **kwargs) -> None: ...
def unique(enumeration: _EnumType) -> _EnumType: ...
