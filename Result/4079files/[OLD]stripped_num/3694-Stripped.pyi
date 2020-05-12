# (generated with --quick)

import __future__
from typing import Any

FLAGS: Any
absolute_import: __future__._Feature
division: __future__._Feature
lt: Any
np: module
os: module
print_function: __future__._Feature
tensorcheck: Any
test_util: Any
tf: Any

class BoundsTest(Any):
    lower_error_lt: Any
    okay_lt: Any
    one_lt: Any
    upper_error_lt: Any
    def setUp(self) -> None: ...
    def test_error(self) -> None: ...
    def test_okay(self) -> None: ...

class ShapeTest(Any):
    correct_lt: Any
    correct_shape_op: Any
    error_lt: Any
    incorrect_lt: Any
    incorrect_shape_op: Any
    okay_lt: Any
    def setUp(self) -> None: ...
    def test_error(self) -> None: ...
    def test_okay(self) -> None: ...

class WellDefinedTest(Any):
    add: Any
    checked_finite_lt: Any
    checked_nan_lt: Any
    finite_lt: Any
    nan_lt: Any
    def setUp(self) -> None: ...
    def test_finite(self) -> None: ...
    def test_nan(self) -> None: ...
