# (generated with --quick)

import contextlib
from typing import Any, Type
import unittest.case

TestCase: Type[unittest.case.TestCase]
Timer: Any
io: module
re: module
redirect_stdout: Type[contextlib.redirect_stdout]
time: module

class BasicTestCase(unittest.case.TestCase):
    def test_basic(self) -> None: ...
    def test_decorator(self) -> None: ...
    def test_elapsed(self) -> None: ...
    def test_multiple_instances(self) -> None: ...
    def test_stdout(self) -> None: ...
