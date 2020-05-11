# (generated with --quick)

from typing import Any, List, NoReturn, Optional, Tuple

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
    board_dimensions: Tuple[int, int]
    colours: Any
    num_columns: int
    num_rows: int
    score_board_height: int
    screen: Any
    size: int
    def __init__(self, size: int, num_columns: int, num_rows: int, score_board_height: int, colours) -> None: ...
    def draw_board(self, balls: List[list], boxes: List[list]) -> None: ...
    def draw_circle(self, position: tuple, colour) -> None: ...
    def draw_score_board(self, score: int, highest_score: int, current_move_score: int, moves: int) -> None: ...
    def end_game(self) -> NoReturn: ...
    def game_over(self, score: int, high_score: int) -> None: ...
    def get_clicked_ball(self) -> Optional[Tuple[int, int]]: ...
    def get_current_ball(self) -> Optional[Tuple[int, int]]: ...
    def get_events(self) -> list: ...
