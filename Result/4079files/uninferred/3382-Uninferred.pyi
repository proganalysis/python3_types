from typing import Any
from unittest import TestCase

class FileAttributeManagerTests(TestCase):
    VALUE_IN_FILE: Any = ...
    filename: Any = ...
    file: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_get(self) -> None: ...
