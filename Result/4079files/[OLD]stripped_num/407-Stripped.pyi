# (generated with --quick)

from typing import Any, NoReturn, Optional, Tuple

BallClickedEvent: Any
Colour: Any
FONT_PATH: str
GAME_OVER_SIZE: int
GameQuit: Any
GuiClient: Any
SCORE_FONT_SIZE: int
math: module
pygame: Any
sys: module

class PyGameClient(Any):
    board_dimensions: Tuple[Any, Any]
    colours: Any
    num_columns: Any
    num_rows: Any
    score_board_height: Any
    screen: Any
    size: Any
    def __init__(self, size, num_columns, num_rows, score_board_height, colours) -> None: ...
    def draw_board(self, balls, boxes) -> None: ...
    def draw_circle(self, position, colour) -> None: ...
    def draw_score_board(self, score, highest_score, current_move_score, moves) -> None: ...
    def end_game(self) -> NoReturn: ...
    def game_over(self, score, high_score) -> None: ...
    def get_clicked_ball(self) -> Optional[Tuple[int, int]]: ...
    def get_current_ball(self) -> Optional[Tuple[int, int]]: ...
    def get_events(self) -> list: ...
