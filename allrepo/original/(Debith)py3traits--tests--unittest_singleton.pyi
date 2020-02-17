# (generated with --quick)

from typing import Any
import unittest.case

Singleton: Any
SingletonError: Any
SingletonInstanceError: Any
unittest: module

class TestSingleton(unittest.case.TestCase):
    def test_enforces_immutability(self) -> None: ...
    def test_second_initialization_with_arguments_are_ignored(self) -> None: ...
    def test_second_initialization_with_kwarguments_are_ignored(self) -> None: ...
    def test_there_can_only_be_one(self) -> None: ...
