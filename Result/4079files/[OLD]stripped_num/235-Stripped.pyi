# (generated with --quick)

from typing import Any, Callable, List, Sequence
import unittest.case

jsonstreamer: Any
unittest: module

class JSONStreamerTests(unittest.case.TestCase):
    _assertions: List[nothing]
    _streamer: Any
    test_simple_object: Callable
    def _catch_all(self, event_name, *args) -> None: ...

class ObjectStreamerListenerTests(unittest.case.TestCase):
    _streamer: Any
    test_on_element: Callable
    test_on_element_multiple_parses: Callable

class ObjectStreamerTests(unittest.case.TestCase):
    _assertions: List[nothing]
    _streamer: Any
    test_arbit_1: Callable
    test_array: Callable
    test_nested_dict: Callable
    test_space_preservation: Callable
    test_spl_chars_in_value: Callable
    def _assert_value(self, expected_value, value) -> None: ...
    def _catch_all(self, event_name, *args) -> None: ...

def json_file_name(test_fn) -> str: ...
def load_test_data(func) -> Callable: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
