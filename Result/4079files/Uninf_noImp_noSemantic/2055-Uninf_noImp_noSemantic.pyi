from src.player.IBot import *
from src.action.IAction import *
from src.Path import *
from typing import Any

class RunnerBot(IBot):
    def play(self, board: Any) -> IAction: ...
