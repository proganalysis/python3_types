# (generated with --quick)

from typing import Any, Tuple

BaseNet: Any
F: Any
SNConv2d: Any
SNLinear: Any
View: Any
finish_layer_2d: Any
logger: logging.Logger
logging: module
nn: Any

class SimpleConvEncoder(Any):
    def __init__(self, shape, dim_out = ..., dim_h = ..., fully_connected_layers = ..., nonlinearity = ..., output_nonlinearity = ..., f_size = ..., stride = ..., pad = ..., min_dim = ..., n_steps = ..., normalize_input = ..., spectral_norm = ..., last_conv_nonlinearity = ..., last_batchnorm = ..., **layer_args) -> None: ...
    def next_size(self, dim_x, dim_y, k, s, p) -> Tuple[Any, Any]: ...

class SimpleNet(Any):
    conv1: Any
    conv2: Any
    conv2_drop: Any
    fc1: Any
    fc2: Any
    def __init__(self) -> None: ...
    def forward(self, x) -> Any: ...

def infer_conv_size(w, k, s, p) -> Any: ...
