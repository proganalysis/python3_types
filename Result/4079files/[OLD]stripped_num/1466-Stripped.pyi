# (generated with --quick)

from typing import Any, Callable, Generator, Tuple
import unittest.case

CoolProp: Any
PropsSI: Any
nose: Any
np: module
unittest: module

class PropsFailures(unittest.case.TestCase):
    def testMatrix(self) -> None: ...
    def testUnmatchedLengths(self) -> None: ...

def check_type(fluid, Tvals) -> None: ...
def test_input_types() -> Generator[Tuple[Callable[[Any, Any], Any], str, Any], Any, None]: ...
