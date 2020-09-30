# (generated with --quick)

from typing import Any

Activation: Any
Dense: Any
Input: Any
K: Any
Lambda: Any
Model: Any
add: Any
concatenate: Any
multiply: Any

class AttentionDecoderCell(Any):
    hidden_dim: Any
    input_ndim: int
    def __init__(self, hidden_dim = ..., **kwargs) -> None: ...
    def build_model(self, input_shape) -> Any: ...

class LSTMDecoderCell(Any):
    hidden_dim: Any
    def __init__(self, hidden_dim = ..., **kwargs) -> None: ...
    def build_model(self, input_shape) -> Any: ...

def __getattr__(name) -> Any: ...
