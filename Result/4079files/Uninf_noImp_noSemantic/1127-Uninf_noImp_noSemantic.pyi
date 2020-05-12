import unittest
from thingflow.filters.combinators import passthrough as passthrough
from typing import Any

MACHINE: Any
TSL2591_INSTALLED: bool
values: Any

class TestRpi(unittest.TestCase):
    def test_gpio(self): ...
    def test_tsl2591(self) -> None: ...
