# (generated with --quick)

from typing import Any, Callable, List, Tuple

MXNetError: Any
assert_almost_equal: Any
keys: List[int]
mx: Any
nose: Any
np: module
py_str: Any
rand_ndarray: Any
shape: Tuple[int, int]
str_keys: List[str]
test_aggregator: Any
test_get_type: Any
test_init: Any
test_invalid_pull: Any
test_list_kv_pair: Any
test_row_sparse_pull: Any
test_single_kv_pair: Any
test_sparse_aggregator: Any
test_updater: Any
unittest: module

def assertRaises(expected_exception, func, *args, **kwargs) -> None: ...
def check_diff_to_scalar(A, x) -> None: ...
def init_kv(stype = ...) -> Any: ...
def init_kv_with_str(stype = ...) -> Any: ...
def setup_module() -> None: ...
def str_updater(key, recv, local) -> None: ...
def teardown() -> None: ...
def updater(key, recv, local) -> None: ...
def with_seed(seed = ...) -> Callable[[Any], Any]: ...
