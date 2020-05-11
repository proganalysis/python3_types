# (generated with --quick)

import numpy
from typing import Any, List, Optional, SupportsFloat

_EOS_ID: int
_PAD_ID: int
np: module

class GetBatch(object):
    __doc__: str
    batch: None
    batch_size: Any
    big_batch: Any
    big_batch_step: int
    data_inp: list
    data_out: Any
    data_spc: Any
    local_step: Any
    max_batch_step: int
    perm: Any
    perm_index: Any
    prepare_batch_index: list
    prepare_inp: list
    prepare_inp_bucket: list
    prepare_inp_mask_bucket: list
    prepare_out: list
    prepare_out_bucket: list
    prepare_out_mask_bucket: list
    prepare_spc: list
    prepare_spc_bucket: List[numpy.ndarray]
    run_through: int
    samples: int
    def __init__(self, data, batch_size, big_batch = ...) -> None: ...
    def get_batch(self) -> Optional[tuple]: ...
    def shuffle(self, real_shuffle = ...) -> None: ...

def ceil(__x: SupportsFloat) -> int: ...
def floor(__x: SupportsFloat) -> int: ...
