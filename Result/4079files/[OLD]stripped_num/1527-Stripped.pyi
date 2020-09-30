# (generated with --quick)

import __future__
from typing import Any, List, Type
import unittest.case
import unittest.suite

TBinaryProtocol: Any
TSocket: Any
TTransport: Any
ThriftTest: Any
absolute_import: __future__._Feature
division: __future__._Feature
glob: module
lib_path: List[str]
print_function: __future__._Feature
sys: module
time: module
unicode_literals: __future__._Feature
unittest: module
xrange: Type[range]

class TestEof(unittest.case.TestCase):
    data: Any
    def eofTestHelper(self, pfactory) -> None: ...
    def eofTestHelperStress(self, pfactory) -> None: ...
    def testBinaryProtocolAcceleratedEof(self) -> None: ...
    def testBinaryProtocolEof(self) -> None: ...
    def testTransportReadAll(self) -> None: ...

def __getattr__(name) -> Any: ...
def suite() -> unittest.suite.TestSuite: ...
