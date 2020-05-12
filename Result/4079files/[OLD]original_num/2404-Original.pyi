# (generated with --quick)

from typing import Any, Type
import unittest.case

NistBeaconValue: Any
TestCase: Type[unittest.case.TestCase]
local_record_json_db: Any
local_record_xml_db: Any

class TestXml(unittest.case.TestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_from_xml(self) -> None: ...
    def test_from_xml_errors(self) -> None: ...
    def test_to_xml(self) -> None: ...
