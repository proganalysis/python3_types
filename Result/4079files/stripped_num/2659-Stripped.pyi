# (generated with --quick)

import _importlib_modulespec
from typing import Any, Callable, Optional
import unittest.case

htmlark: Any
importlib: module
os: module
requests_available: bool
requests_spec: Optional[_importlib_modulespec.ModuleSpec]
unittest: module

class TestHTMLArk(unittest.case.TestCase):
    __doc__: str
    test_get_resource: Callable
    def test_get_resource_errors(self) -> None: ...
    def test_make_data_uri(self) -> None: ...
