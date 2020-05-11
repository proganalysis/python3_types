# (generated with --quick)

from typing import Any, List, TypeVar, Union

Interfaces: Any
Nodes: Any
TaskManager: Any
concurrent: module
end_map_time: float
end_submit_time: float
exSheet: Any
logger: logging.Logger
logging: module
map_run_time: float
start_map_time: float
start_submit_time: float
submit_run_time: float
sys: module
tasks_needed: int
time: module

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')

def ex(a: _T0, b: _T1) -> List[Union[bool, _T0, _T1]]: ...
def map_test(tasks_needed, chuncksize = ...) -> None: ...
def start_node() -> Any: ...
def submit_test(tasks_needed) -> None: ...
