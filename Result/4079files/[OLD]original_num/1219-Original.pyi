# (generated with --quick)

import hashlib
from typing import Any, Union
import unittest.case

dh: Any
ec: Any
mult: Any
octets_from_int: Any
octets_from_point: Any
point_from_octets: Any
unittest: module

class TestEcdh(unittest.case.TestCase):
    def test_ecdh(self) -> None: ...
    def test_key_deployment(self) -> None: ...

def hf(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
