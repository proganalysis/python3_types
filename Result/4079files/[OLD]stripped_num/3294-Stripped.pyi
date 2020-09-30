# (generated with --quick)

from typing import Any
import unittest.case

Bernoulli: Any
Constant: Any
DGP: Any
DGP_Base: Any
DGP_Heinonen: Any
DGP_Quad: Any
GPMC_Layer: Any
GPR: Any
GPR_Layer: Any
Gaussian: Any
Identity: Any
Linear: Any
Matern52: Any
MultiClass: Any
NatGradOptimizer: Any
RBF: Any
SVGP: Any
ScipyOptimizer: Any
Zero: Any
_session_manager: Any
_settings: Any
assert_allclose: Any
custom_config: Any
init_layers_linear: Any
np: module
settings: Any
unittest: module

class TestHeinonen(unittest.case.TestCase):
    D_Y: int
    X: Any
    Xs: Any
    def test_vs_DGP2(self) -> None: ...
    def test_vs_single_layer(self) -> None: ...
