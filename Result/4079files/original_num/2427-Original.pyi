# (generated with --quick)

from typing import Any, Dict, Optional, Tuple, TypeVar

__author__: str
shuffle: Any

_T = TypeVar('_T')
_TBatchGenerator = TypeVar('_TBatchGenerator', bound=BatchGenerator)

class BatchGenerator(object):
    _X: Any
    __doc__: str
    _batch_id: int
    _batch_size: Any
    _data_size: int
    _finish: bool
    _shuffle: Any
    _valid: Any
    _y: Any
    def __init__(self, X, y, batch_size, shuffle = ..., valid = ...) -> None: ...
    def __iter__(self: _TBatchGenerator) -> _TBatchGenerator: ...
    def __next__(self) -> Tuple[Any, Any]: ...
    def _gen_batch(self, batch_id, batch_size, data_size) -> Tuple[Any, Any]: ...

def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
