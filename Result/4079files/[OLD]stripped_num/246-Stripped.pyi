# (generated with --quick)

from typing import Any, List, Optional

Client: Any
LocalCluster: Any
log: logging.Logger
logging: module
os: module

def findNodes(c) -> list: ...
def get_dask_Client(timeout = ..., n_workers = ..., threads_per_worker = ..., processes = ..., create_cluster = ..., memory_limit = ..., local_dir = ..., with_file = ..., scheduler_file = ..., dashboard_address = ...) -> Any: ...
def get_nodes() -> Optional[List[str]]: ...
