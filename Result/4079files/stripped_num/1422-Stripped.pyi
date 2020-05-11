# (generated with --quick)

from typing import Any
import unittest.case

Bernoulli: Any
DGP: Any
DGP_Base: Any
DGP_Collapsed: Any
DGP_Quad: Any
GPR: Any
Gaussian: Any
Matern52: Any
MultiClass: Any
NatGradOptimizer: Any
RBF: Any
SGPR_Layer: Any
SVGP: Any
ScipyOptimizer: Any
assert_allclose: Any
init_layers_linear: Any
np: module
unittest: module

class TestVsNatGrads(unittest.case.TestCase):
    def test_2layer_vs_nat_grad(self) -> None: ...

class TestVsSingleLayer(unittest.case.TestCase):
    D_Y: int
    X: Any
    Xs: Any
    Y: Any
    Z: Any
    lik_var: float
    def test_single_layer(self) -> None: ...
