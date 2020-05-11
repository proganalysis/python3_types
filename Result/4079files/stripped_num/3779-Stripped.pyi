# (generated with --quick)

import enum
from typing import Any, Tuple, Type

CELL_SIZE: int
Enum: Type[enum.Enum]
HEIGHT: Any
WIDTH: Any
WINDOW_HEIGHT: Any
WINDOW_WIDTH: Any
font: Any
pygame: Any
screen: Any

class COLOR(enum.Enum):
    BG_COLOR: Tuple[int, int, int]
    BLACK: Tuple[int, int, int]
    DARK_GRAY: Tuple[int, int, int]
    DARK_GREEN: Tuple[int, int, int]
    GREEN: Tuple[int, int, int]
    RED: Tuple[int, int, int]
    WHITE: Tuple[int, int, int]

def draw_bg() -> None: ...
def draw_cell(cell, color = ...) -> None: ...
def draw_cell_line(cells, cell_color = ..., line_color = ...) -> None: ...
def draw_cells(cells, color = ...) -> None: ...
def draw_grid() -> None: ...
def init(title, width = ..., height = ...) -> None: ...
def update() -> None: ...
