# (generated with --quick)

from typing import Any

DataHolder: Any
GPModel: Any
Gaussian: Any
Parameter: Any
conditional: Any
np: module
params_as_tensors: Any
settings: Any
tf: Any

class GPMC(Any):
    V: Any
    _build_likelihood: Any
    _build_predict: Any
    num_data: Any
    def __init__(self, X, Y, kern, likelihood, mean_function = ..., num_latent = ..., **kwargs) -> None: ...
    def compile(self, session = ...) -> Any: ...
