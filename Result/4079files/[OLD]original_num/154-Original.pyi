# (generated with --quick)

from typing import Any, Coroutine, Dict, List, Union

Config: Any
__author__: str
__version__: str
asyncio: module
bank: Any
checks: Any
commands: Any
discord: Any
itertools: module
outputs: Any
random: module

class RussianRoulette(Any):
    chamber: Any
    cost: Any
    db: Any
    defaults: Dict[str, Union[int, Dict[str, Union[int, List[nothing]]]]]
    rusreset: Any
    russian: Any
    russianversion: Any
    setrussian: Any
    wait: Any
    def __init__(self) -> None: ...
    def add_player(self, ctx, cost) -> Coroutine[Any, Any, None]: ...
    def game_checks(self, ctx, settings) -> Coroutine[Any, Any, bool]: ...
    def game_teardown(self, ctx, players) -> Coroutine[Any, Any, None]: ...
    def reset_game(self, ctx) -> Coroutine[Any, Any, None]: ...
    def start_game(self, ctx) -> coroutine: ...
    def start_round(self, ctx, chamber, players) -> Coroutine[Any, Any, None]: ...
