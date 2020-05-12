# (generated with --quick)

from typing import Any, Type
import unittest.case

Boolean: Any
InvalidConfiguration: Any
List: Any
Option: Any
TestCase: Type[unittest.case.TestCase]
Tuple: Any
config: Any

class BooleanCastTestCase(unittest.case.TestCase):
    def test_basic_boolean_cast(self) -> None: ...
    def test_fail_invalid_boolean_cast(self) -> None: ...
    def test_more_valid_boolean_values(self) -> None: ...

class EvalCastTestCase(unittest.case.TestCase):
    def test_if_cast_is_unbounded(self) -> None: ...

class OptionCastTestCase(unittest.case.TestCase):
    def test_fail_invalid_option_config(self) -> None: ...
    def test_options(self) -> None: ...

class SequenceCastTestCase(unittest.case.TestCase):
    def test_basic_list_cast(self) -> None: ...
    def test_basic_tuple_cast(self) -> None: ...
