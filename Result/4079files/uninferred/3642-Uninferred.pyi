from UliEngineering.Utils.JSON import *
from numpy.testing import assert_approx_equal as assert_approx_equal

class TestNumpyEncoder:
    def testNDArrayEncoding(self) -> None: ...
    def testNDMultidimensionalArrayEncoding(self) -> None: ...
    def testNPScalarEncoding(self) -> None: ...
    def testOtherEncoding(self) -> None: ...
    def test_invalid_encoding(self) -> None: ...