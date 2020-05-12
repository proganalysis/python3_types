# (generated with --quick)

from typing import Any, Dict, Tuple, TypeVar, Union

Chain: Any
F: Any
L: Any
State: Any
Variable: Any

_T1 = TypeVar('_T1')

class Classifier(Any):
    def __call__(self, words, state = ..., dropout = ..., train = ...) -> Any: ...
    def __init__(self, predictor) -> None: ...
    def loss(self, words, state, dropout = ..., train = ...) -> Any: ...

class RNN(Any):
    embed_dim: Any
    gpu: Any
    h_units: Any
    n_units: Any
    def __call__(self, words, state, dropout = ..., train = ...) -> Tuple[list, Any]: ...
    def __init__(self, embed_dim, n_units = ..., h_units = ..., gpu = ...) -> None: ...
    def forward(self, words, state: _T1, dropout = ..., train = ...) -> Tuple[list, Union[Dict[str, Any], _T1]]: ...
    def forward_one(self, word, state, dropout = ..., train = ...) -> Tuple[Any, Dict[str, Any]]: ...
