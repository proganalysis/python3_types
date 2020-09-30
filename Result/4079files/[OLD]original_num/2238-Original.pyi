# (generated with --quick)

from typing import Any, Tuple, Type

Chain: Any
Classifier: Type[rnn.Classifier]
F: Any
L: Any
State: Any
Variable: Any
rnn: module

class LSTM(Any):
    embed_dim: int
    gpu: int
    n_units: int
    def __call__(self, words: list, state, dropout: bool = ..., train: bool = ...) -> Tuple[list, Any]: ...
    def __init__(self, embed_dim: int, n_units: int = ..., gpu: int = ...) -> None: ...
    def forward(self, words: list, state, dropout: bool = ..., train: bool = ...) -> Tuple[list, Any]: ...
    def forward_one(self, word, state, dropout: bool = ..., train: bool = ...) -> Tuple[Any, Any]: ...
    def reset_state(self) -> None: ...
    def set_word_embedding(self, array) -> None: ...
