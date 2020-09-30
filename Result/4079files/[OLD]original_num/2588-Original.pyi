# (generated with --quick)

from typing import Any, Dict, Optional, TypeVar
import unittest.case

Model: Any
unittest: module

_T = TypeVar('_T')

class Prototype(Any):
    value: str
    def clone(self, **attrs) -> Any: ...

class TestPrototype(unittest.case.TestCase):
    prototype: Prototype
    def test_dispatcher(self) -> None: ...

def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
