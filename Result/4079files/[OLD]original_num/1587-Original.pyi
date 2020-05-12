# (generated with --quick)

from typing import Any
import unittest.mock

L4Proto: Any
SCIONAddr: Any
SCIONChecksumFailed: Any
SCIONUDPHeader: Any
SCMPBadPktLen: Any
create_mock: Any
create_mock_full: Any
nose: Any
ntools: Any
patch: unittest.mock._patcher

class TestSCIONUDPHeaderCalcChecksum(object):
    __doc__: str
    test: Any

class TestSCIONUDPHeaderParse(object):
    __doc__: str
    test: Any

class TestSCIONUDPHeaderReverse(object):
    __doc__: str
    def test(self) -> None: ...

class TestSCIONUDPHeaderValidate(object):
    __doc__: str
    test_bad_checksum: Any
    test_bad_length: Any
