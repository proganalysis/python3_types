# (generated with --quick)

from typing import Any, Dict, Tuple, Type, TypeVar, Union

Chain: Any
Classifier: Type[rnn.Classifier]
F: Any
L: Any
State: Any
Variable: Any
rnn: module

_T1 = TypeVar('_T1')

class LSTM(Any):
    embed_dim: Any
    gpu: Any
    n_units: Any
    def __call__(self, words, state, dropout = ..., train = ...) -> Tuple[list, Any]: ...
    def __init__(self, embed_dim, n_units = ..., gpu = ...) -> None: ...
    def forward(self, words, state: _T1, dropout = ..., train = ...) -> Tuple[list, Union[Dict[str, Any], _T1]]: ...
    def forward_one(self, word, state, dropout = ..., train = ...) -> Tuple[Any, Dict[str, Any]]: ...
    def reset_state(self) -> None: ...
    def set_word_embedding(self, array) -> None: ...
