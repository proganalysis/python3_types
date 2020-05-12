# (generated with --quick)

from typing import Any, Type
import unittest.case

INIData: Any
StorageManager: Any
TestCase: Type[unittest.case.TestCase]
__author__: str
assert_equal: Any
assert_raises: Any
assert_true: Any
os: module
secrets: module
shutil: module
tempfile: module

class TestINI(unittest.case.TestCase):
    config_dir: str
    data_dir: str
    directory: str
    manager: Any
    def test_read(self) -> None: ...
    def test_write(self) -> None: ...
