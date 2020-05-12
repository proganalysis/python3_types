# (generated with --quick)

from typing import Any, Dict, Tuple

tf: Any

class ContentAttention(object):
    __doc__: str
    alignments_history: Any
    batch_size: Any
    e_bias_neg: Any
    e_bias_zero: Any
    e_range_seq: Any
    enc_length: Any
    enc_units: Any
    hidden_feats: Any
    memory: Any
    name: Any
    sequence_length: Any
    units: Any
    def __call__(self, query, state_tm1) -> Tuple[Any, Dict[str, Any]]: ...
    def __init__(self, memory, sequence_length, units, alignments_history = ..., name = ...) -> None: ...
    def zero_state(self, batch_size, dtype) -> Dict[str, Any]: ...

class GMMAttention(object):
    __doc__: str
    alignments_history: Any
    batch_size: Any
    enc_length: Any
    enc_units: Any
    init_kappa_pos: Any
    mask: Any
    memory: Any
    name: Any
    sequence_length: Any
    tmp_l: Any
    units: Any
    def __call__(self, query, state_tm1) -> Tuple[Any, Dict[str, Any]]: ...
    def __init__(self, memory, sequence_length, units, alignments_history = ..., init_kappa_pos = ..., name = ...) -> None: ...
    def zero_state(self, batch_size, dtype) -> Dict[str, Any]: ...

class MultiHeadAttentionWrapper(object):
    att_mod_list: Any
    name: Any
    def __call__(self, query, state_lst_tm1, reuse = ...) -> Tuple[Any, list]: ...
    def __init__(self, att_mod_list, name = ...) -> None: ...
    def zero_state(self, batch_size, dtype) -> list: ...

def bias_seq(inputs, sequence_length, bias = ..., name = ...) -> Any: ...
def mask_seq(inputs, sequence_length, name = ...) -> Any: ...
