# (generated with --quick)

from typing import Any, Dict, Tuple

Chain: Any
F: Any
L: Any
State: Any
Variable: Any

class Classifier(Any):
    def __call__(self, words: int, state = ..., dropout: bool = ..., train: bool = ...) -> Tuple[Any, Dict[str, Any], Any]: ...
    def __init__(self, predictor) -> None: ...
    def loss(self, words, state, dropout: bool = ..., train: bool = ...) -> Any: ...

class RNN(Any):
    embed_dim: int
    gpu: int
    h_units: int
    n_units: int
    def __call__(self, words: list, state, dropout: bool = ..., train: bool = ...) -> Tuple[list, Any]: ...
    def __init__(self, embed_dim: int, n_units: int = ..., h_units: int = ..., gpu: int = ...) -> None: ...
    def forward(self, words: list, state, dropout: bool = ..., train: bool = ...) -> Tuple[list, Any]: ...
    def forward_one(self, word, state, dropout: bool = ..., train: bool = ...) -> Tuple[Any, Any]: ...
