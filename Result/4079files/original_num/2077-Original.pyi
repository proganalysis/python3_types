# (generated with --quick)

from typing import Any, SupportsFloat, Tuple
import unittest.case

ConstantMean: Any
GaussianLikelihood: Any
GridInterpolationKernel: Any
MultivariateNormal: Any
RBFKernel: Any
ScaleKernel: Any
SmoothedBoxPrior: Any
data_dim: int
feature_extractor: SmallFeatureExtractor
gpytorch: Any
nn: Any
optim: Any
os: module
pi: float
random: module
torch: Any
unittest: module

class GPRegressionModel(Any):
    base_covar_module: Any
    covar_module: Any
    feature_extractor: SmallFeatureExtractor
    mean_module: Any
    def __init__(self, train_x, train_y, likelihood) -> None: ...
    def forward(self, x) -> Any: ...

class SmallFeatureExtractor(Any):
    def __init__(self) -> None: ...

class TestDKLRegression(unittest.case.TestCase):
    rng_state: Any
    def test_dkl_gp_fast_pred_var(self) -> None: ...
    def test_dkl_gp_mean_abs_error(self) -> None: ...

def exp(__x: SupportsFloat) -> float: ...
def make_data(cuda = ...) -> Tuple[Any, Any, Any, Any]: ...
