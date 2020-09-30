# (generated with --quick)

from typing import Any, List, Type
import unittest.case

DataBankMixin: Any
IMAGING: Any
TestCase: Type[unittest.case.TestCase]
load_log: Any

class TestLogBank(Any, unittest.case.TestCase):
    DATA_DIR: List[str]
    print_success_path: bool
    def file_should_be_processed(self, filepath) -> Any: ...
    def test_all(self) -> None: ...

def run_log(path) -> str: ...
