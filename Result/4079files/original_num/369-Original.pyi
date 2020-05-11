# (generated with --quick)

from typing import Any

BroadcastingLikelihood: Any
DataHolder: Any
GPMC_Layer: Any
GPR_Layer: Any
Gaussian: Any
Identity: Any
Linear: Any
Minibatch: Any
Model: Any
ParamList: Any
SGPMC_Layer: Any
SVGP_Layer: Any
Zero: Any
autoflow: Any
float_type: Any
init_layers_linear: Any
mvhermgauss: Any
np: module
params_as_tensors: Any
reparameterize: Any
settings: Any
tf: Any

class DGP(DGP_Base):
    X: Any
    Y: Any
    __doc__: str
    layers: Any
    likelihood: Any
    num_data: Any
    num_samples: int
    def __init__(self, X, Y, Z, kernels, likelihood, num_outputs = ..., mean_function = ..., white = ..., **kwargs) -> None: ...

class DGP_Base(Any):
    X: Any
    Y: Any
    __doc__: str
    _build_likelihood: Any
    _build_predict: Any
    layers: Any
    likelihood: Any
    num_data: Any
    num_samples: Any
    predict_all_layers: Any
    predict_all_layers_full_cov: Any
    predict_density: Any
    predict_f: Any
    predict_f_full_cov: Any
    predict_y: Any
    propagate: Any
    def E_log_p_Y(self, X, Y) -> Any: ...
    def __init__(self, X, Y, likelihood, layers, minibatch_size = ..., num_samples = ..., num_data = ..., **kwargs) -> None: ...

class DGP_Quad(DGP_Base):
    D_quad: Any
    H: Any
    X: Any
    Y: Any
    __doc__: str
    gh_w: Any
    gh_x: list
    layers: Any
    likelihood: Any
    num_data: Any
    num_samples: int
    def __init__(self, *args, H = ..., **kwargs) -> None: ...
