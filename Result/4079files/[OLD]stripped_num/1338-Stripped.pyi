# (generated with --quick)

import __future__
from typing import Any, Callable

_BUCKET_LENGTH_STEP: int
_BUCKET_MAX_BOUNDARY: int
_BUCKET_MIN_BOUNDARY: int
_CHAR_TO_FILTER_OUT: str
_SHUFFLE_BUFFER_SIZE: int
absolute_import: __future__._Feature
constants: Any
division: __future__._Feature
multiprocessing: module
np: module
print_function: __future__._Feature
tf: Any
utils: Any

def get_sparse_tensor_size(tensor) -> Any: ...
def group_by_sequence_length_sparse(element_length_func, bucket_boundaries, batch_size) -> Any: ...
def make_input_fn(input_dir, batch_size, training = ..., num_epochs = ..., random_seed = ..., prefetch_buffer_size = ...) -> Callable[[], Any]: ...
def parse_raw_text(sentence) -> dict: ...
def serving_input_fn() -> Any: ...
