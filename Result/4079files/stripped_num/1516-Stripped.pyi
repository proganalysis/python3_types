# (generated with --quick)

from typing import Any, Dict, List, Optional, TextIO, TypeVar

Extension: Any
build_ext: Any
ext_modules: list
f: TextIO
find_packages: Any
here: str
long_description: str
os: module
setup: Any
setuptools: module
sys: module
sysconfig: module

_T = TypeVar('_T')

class BuildExt(Any):
    __doc__: str
    c_opts: Dict[str, List[str]]
    def build_extensions(self) -> None: ...
    def finalize_options(self) -> None: ...

def cpp_flag(compiler) -> str: ...
def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def has_flag(compiler, flagname) -> bool: ...
