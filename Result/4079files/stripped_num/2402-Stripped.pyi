# (generated with --quick)

from typing import Any, List

gym: Any
os: module
random: module

class Hanamichi:
    actions: List[int]
    fun: Any
    def __init__(self) -> None: ...
    def act(self, observation, last_reward) -> int: ...
    def end(self, last_reward) -> None: ...
    def start(self, observation) -> Any: ...

def main(game_count = ...) -> None: ...
