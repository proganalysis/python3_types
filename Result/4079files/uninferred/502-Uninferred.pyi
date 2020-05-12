from common import setup_module as setup_module, teardown as teardown
from typing import Any

shape: Any
keys: Any
str_keys: Any

def init_kv(stype: str = ...): ...
def init_kv_with_str(stype: str = ...): ...
def check_diff_to_scalar(A: Any, x: Any) -> None: ...
def test_single_kv_pair() -> None: ...
def test_row_sparse_pull() -> None: ...
def test_init() -> None: ...
def test_list_kv_pair() -> None: ...
def test_aggregator() -> None: ...
def test_sparse_aggregator() -> None: ...
def updater(key: Any, recv: Any, local: Any) -> None: ...
def str_updater(key: Any, recv: Any, local: Any) -> None: ...
def test_updater(dev: str = ...) -> None: ...
def test_get_type() -> None: ...
def test_invalid_pull() -> None: ...
