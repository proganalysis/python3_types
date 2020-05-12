import unittest
from typing import Any

requests_spec: Any
requests_available: Any

class TestHTMLArk(unittest.TestCase):
    def test_make_data_uri(self) -> None: ...
    def test_get_resource(self) -> None: ...
    def test_get_resource_errors(self) -> None: ...
