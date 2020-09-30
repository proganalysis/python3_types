# (generated with --quick)

from typing import Any
import unittest.case

ODIE_DIR: str
app: Any
config: Any
fill_data: Any
json: module
os: module
sqla: Any
subprocess: module
unittest: module

class OdieTestCase(unittest.case.TestCase):
    original_items_per_page: Any
    @staticmethod
    def clear_all() -> None: ...
    def disable_pagination(self) -> None: ...
    def enable_pagination(self, items_per_page = ...) -> None: ...
    def fromJsonResponse(self, response) -> Any: ...
    def logout(self) -> Any: ...
    @classmethod
    def setUpClass(cls) -> None: ...
