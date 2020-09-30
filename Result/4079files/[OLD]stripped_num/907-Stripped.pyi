# (generated with --quick)

from typing import Any, List, Tuple, TypeVar

_FOGLAMP_PLUGIN_PATH: Any
_FOGLAMP_ROOT: Any
_lib_path: Any
_logger: Any
json: module
logger: Any
os: module
subprocess: module

_T0 = TypeVar('_T0')

def _find_c_lib(name, dir) -> Any: ...
def _find_c_util(name) -> Any: ...
def _find_plugins_from_env(_plugin_path: _T0) -> _T0: ...
def find_c_plugin_libs(direction) -> List[Tuple[Any, str]]: ...
def get_plugin_info(name, dir) -> Any: ...
