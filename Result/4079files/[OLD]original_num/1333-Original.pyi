# (generated with --quick)

from typing import Any, Tuple

Gamma: Any
MVN_LAZY_PROPERTIES: Tuple[str, str, str]
MultivariateNormal: Any
Normal: Any
Prior: Any
TModule: Any
_bufferize_attributes: Any
_del_attributes: Any

class GammaPrior(Any, Any):
    __doc__: str
    _transform: Any
    def __init__(self, concentration, rate, validate_args = ..., transform = ...) -> None: ...

class MultivariateNormalPrior(Any, Any):
    __doc__: str
    _transform: Any
    def __init__(self, loc, covariance_matrix = ..., precision_matrix = ..., scale_tril = ..., validate_args = ..., transform = ...) -> None: ...
    def cpu(self) -> Any: ...
    def cuda(self, device = ...) -> Any: ...

class NormalPrior(Any, Any):
    __doc__: str
    _transform: Any
    def __init__(self, loc, scale, validate_args = ..., transform = ...) -> None: ...
