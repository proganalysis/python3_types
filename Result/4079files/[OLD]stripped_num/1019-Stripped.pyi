# (generated with --quick)

import isolation.isolation
from typing import Any, List, Tuple, Type

Board: Type[isolation.isolation.Board]
game: isolation.isolation.Board
history: List[list]
logging: module
new_game: Any
outcome: str
player1: RandomPlayer
player2: GreedyPlayer
winner: Any

class GreedyPlayer:
    __doc__: str
    score: Any
    def __init__(self, score_fn = ...) -> None: ...
    def get_move(self, game, legal_moves, time_left) -> Any: ...

class HumanPlayer:
    __doc__: str
    name: str
    def __init__(self) -> None: ...
    def get_move(self, game, legal_moves, time_left) -> Tuple[int, int]: ...

class RandomPlayer:
    __doc__: str
    def get_move(self, game, legal_moves, time_left) -> Any: ...

def improved_score(game, player) -> float: ...
def null_score(game, player) -> float: ...
def open_move_score(game, player) -> float: ...
def randint(a: int, b: int) -> int: ...
def show_instructions() -> None: ...
