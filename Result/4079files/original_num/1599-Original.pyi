# (generated with --quick)

from typing import Any, TypeVar

CATALOG_PATH: str
DATA_DIR: str
DESCR: str
Data: Any
PATH: str
URL: str
base: Any
bz2: module
np: module
os: module
pd: Any
tarfile: module
warnings: module

_T0 = TypeVar('_T0')

def _check_dim(lc: _T0) -> _T0: ...
def _get_OGLE3_data_home(data_home) -> str: ...
def fetch_OGLE3(ogle3_id, data_home = ..., metadata = ..., download_if_missing = ...) -> Any: ...
def load_OGLE3_catalog() -> Any: ...
