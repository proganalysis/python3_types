import enum
import fsm
import unittest
from typing import Any

class MyFsm(fsm.StateMachine):
    class State(enum.Enum):
        start: int = ...
        running: int = ...
        done: int = ...
    class SubState(enum.Enum):
        running_substate: int = ...
    _log: Any = ...
    def __init__(self): ...
    def on_enter_start(self) -> None: ...
    def on_enter_running(self) -> None: ...
    def on_enter_done(self) -> None: ...
    def on_enter_running_substate(self) -> None: ...
    def on_exit_start(self) -> None: ...
    def on_exit_running(self) -> None: ...
    def on_exit_done(self) -> None: ...
    def on_exit_running_substate(self) -> None: ...
    def execute_start(self) -> None: ...
    def execute_running(self) -> None: ...
    def execute_done(self) -> None: ...
    def execute_running_substate(self) -> None: ...

class TestFsm(unittest.TestCase):
    def test_transisions(self) -> None: ...
    def test_ancestor_chain(self) -> None: ...