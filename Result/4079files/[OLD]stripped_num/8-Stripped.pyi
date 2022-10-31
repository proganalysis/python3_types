# (generated with --quick)

from typing import Any, List, Optional, TypeVar

WIN_ALLOW_CROSS_ARCH: bool
__all__: List[str]
os: module
sys: module

_T0 = TypeVar('_T0')

def _get_path_list() -> List[str]: ...
@overload
def find_exe(program) -> Any: ...
@overload
def find_exe(program: _T0) -> Optional[_T0]: ...
def get_path_list() -> List[str]: ...
def is_exe(path) -> bool: ...
def main() -> None: ...
def which(program) -> Any: ...