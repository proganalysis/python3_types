# (generated with --quick)

from typing import Any, Tuple, Type
import unittest.case

PluginCache: Any
TestCase: Type[unittest.case.TestCase]
coverage: Any
pip: module
pytest: Any

class TestPluginCache(unittest.case.TestCase):
    candidates: Tuple[str, str, str]
    def test__cache__actually_caches_things(self) -> None: ...
    def test__cache__attribute_access(self) -> None: ...
    def test__cache__loads_expected_objects(self) -> None: ...
