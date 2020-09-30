# (generated with --quick)

import __future__
from typing import Any

FLAGS: Any
absolute_import: __future__._Feature
data_provider: Any
division: __future__._Feature
flags: Any
lt: Any
print_function: __future__._Feature
test: Any
test_util: Any
tf: Any
util: Any
visualize: Any

class AdditiveErrorTest(ErrorBase):
    additive_lt: Any
    target_lt: Any
    target_lt_0: Any
    target_lt_1: Any
    def test(self) -> None: ...
    def test_name(self) -> None: ...

class CrossEntropyErrorTest(ErrorBase):
    ce_lt: Any
    target_lt: Any
    target_lt_0: Any
    target_lt_1: Any
    def test(self) -> None: ...
    def test_name(self) -> None: ...

class ErrorBase(Any):
    target_lt: Any
    target_lt_0: Any
    target_lt_1: Any
    def setUp(self) -> None: ...

class ErrorPanelTest(Any):
    error_panel_lt: Any
    prediction_lt: Any
    target_lt: Any
    def setUp(self) -> None: ...
    def test(self) -> None: ...
    def test_name(self) -> None: ...

class SubtractiveErrorTest(ErrorBase):
    subtractive_lt: Any
    target_lt: Any
    target_lt_0: Any
    target_lt_1: Any
    def test(self) -> None: ...
    def test_name(self) -> None: ...
