import unittest
from typing import Any
from unittest.mock import MagicMock as MagicMock, _patch_object as _patch_object

class test_yast(unittest.TestCase):
    def test_load_dictionary(self, mocked_file_iterator: Any, mocked_count_line: Any) -> None: ...
    def test_transcode_str_line(self) -> None: ...
    def test_transcode_str_line_with_replacements(self) -> None: ...
    def test_list_replace(self) -> None: ...
    def test_get_replacement_dict(self) -> None: ...
