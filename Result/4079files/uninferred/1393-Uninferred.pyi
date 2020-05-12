import unittest
from typing import Any

EXAMPLE_DEPENDENCY: str
TESTED_DEPENDENCIES: Any

class Tests(unittest.TestCase):
    def test_deps(self) -> None: ...
    def test_cleanup_deps(self) -> None: ...
