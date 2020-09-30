# (generated with --quick)

from typing import Any, TypeVar

Activation: Any
BLACK: Any
Dense: Any
Dropout: Any
EMPTY: Any
Game: Any
Move: Any
RMSprop: Any
Sequential: Any
WHITE: Any
copy: module
np: module
random: module
time: module

_T0 = TypeVar('_T0')

def board2input(game, player) -> Any: ...
def check_dead_group(game, col_coord, row_coord) -> bool: ...
def init_game(game: _T0, col_coord, row_coord) -> _T0: ...
def main() -> None: ...
