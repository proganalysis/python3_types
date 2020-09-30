import unittest
from doubly_stochastic_dgp.dgp import DGP_Base as DGP_Base, DGP_Quad as DGP_Quad
from doubly_stochastic_dgp.layer_initializations import init_layers_linear as init_layers_linear
from gpflow import settings as settings
from gpflow.kernels import RBF as RBF
from gpflow.likelihoods import Bernoulli as Bernoulli, MultiClass as MultiClass
from gpflow.mean_functions import Constant as Constant, Linear as Linear
from gpflow.models import SVGP as SVGP
from gpflow.training import ScipyOptimizer as ScipyOptimizer
from typing import Any

custom_config: Any

class TestHeinonen(unittest.TestCase):
    X: Any = ...
    Xs: Any = ...
    D_Y: Any = ...
    def setUp(self) -> None: ...
    def test_vs_single_layer(self) -> None: ...
    def test_vs_DGP2(self) -> None: ...
