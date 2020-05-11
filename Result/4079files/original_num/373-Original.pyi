# (generated with --quick)

from typing import Any, Type
import unittest.case
import unittest.mock

TestCase: Type[unittest.case.TestCase]
logic: Any
patch: unittest.mock._patcher

class BodyTests(unittest.case.TestCase):
    test_body: Any

class MetadataTests(unittest.case.TestCase):
    test_loads_all_metadata: Any
    test_loads_specific_metadata: Any

class SearchTests(unittest.case.TestCase):
    test_conjunctive_query: Any
    test_query_expands_fields: Any

def _setup_mock_query(mock, *key_values) -> None: ...
