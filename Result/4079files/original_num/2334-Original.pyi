# (generated with --quick)

import __future__
from typing import Any, Tuple

division: __future__._Feature
tf: Any

class CaptionGenerator(object):
    D: Any
    H: Any
    L: Any
    M: Any
    T: Any
    V: int
    _null: Any
    _start: Any
    alpha_c: Any
    captions: Any
    const_initializer: Any
    ctx2out: Any
    dropout: Any
    emb_initializer: Any
    features: Any
    idx_to_word: dict
    prev2out: Any
    selector: Any
    weight_initializer: Any
    word_to_idx: Any
    def __init__(self, word_to_idx, dim_feature = ..., dim_embed = ..., dim_hidden = ..., n_time_step = ..., prev2out = ..., ctx2out = ..., alpha_c = ..., selector = ..., dropout = ...) -> None: ...
    def _attention_layer(self, features, features_proj, h, reuse = ...) -> Tuple[Any, Any]: ...
    def _batch_norm(self, x, mode = ..., name = ...) -> Any: ...
    def _decode_lstm(self, x, h, context, dropout = ..., reuse = ...) -> Any: ...
    def _get_initial_lstm(self, features) -> Tuple[Any, Any]: ...
    def _project_features(self, features) -> Any: ...
    def _selector(self, context, h, reuse = ...) -> Tuple[Any, Any]: ...
    def _word_embedding(self, inputs, reuse = ...) -> Any: ...
    def build_model(self) -> Any: ...
    def build_sampler(self, max_len = ...) -> Tuple[Any, Any, Any]: ...
