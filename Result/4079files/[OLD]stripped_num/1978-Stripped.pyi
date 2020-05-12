# (generated with --quick)

from typing import Any, Tuple
import unittest.case

BaseModel: Any
EI: Any
LCB: Any
LogEI: Any
MarginalizationGPMCMC: Any
PI: Any
np: module
unittest: module

class DemoModel(Any):
    X: Any
    m: Any
    v: Any
    y: Any
    def __init__(self, m, v) -> None: ...
    def predict(self, X_test) -> Tuple[Any, Any]: ...
    def train(self, X, y) -> None: ...

class DemoModelMCMC(Any):
    models: Any
    n_hypers: int
    predict: Any
    train: Any
    def __init__(self) -> None: ...

class TestMarginalizationGPMCMC(unittest.case.TestCase):
    X: Any
    model: DemoModelMCMC
    y: Any
    def test_ei(self) -> None: ...
    def test_lcb(self) -> None: ...
    def test_log_ei(self) -> None: ...
    def test_pi(self) -> None: ...
