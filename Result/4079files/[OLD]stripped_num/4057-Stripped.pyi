# (generated with --quick)

from typing import Any
import unittest.case

Goban: Any
MagicMock: Any
Move: Any
unittest: module

class TestVoteMove(unittest.case.TestCase):
    a1_move: Any
    a2_move: Any
    goban: Any
    random_move: Any
    def test_already_voted(self) -> None: ...
    def test_change_vote(self) -> None: ...
    def test_invalid_move(self) -> None: ...
    def test_vote_random(self) -> None: ...
    def test_vote_succeeds(self) -> None: ...
