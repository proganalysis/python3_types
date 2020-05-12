import unittest
from typing import Any

class TestPluginManager(unittest.TestCase):
    plugin: Any = ...
    pm: Any = ...
    def setUp(self) -> None: ...
    def test_plugins(self) -> None: ...
    def test_semantic_types(self) -> None: ...
    def test_importable_types(self) -> None: ...
    def test_importable_formats(self) -> None: ...
    def test_importable_formats_excludes_unimportables(self) -> None: ...
