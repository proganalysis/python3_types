from numba.cuda.testing import SerialMixin, unittest

class TestCudaArrayArg(SerialMixin, unittest.TestCase):
    def test_array_ary(self): ...
