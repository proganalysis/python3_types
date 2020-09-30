# (generated with --quick)

import __future__
from typing import Any, Callable, Dict, List, Optional

COMPILE_OPTIONS: Dict[str, List[str]]
Extension: Any
LINK_OPTIONS: Dict[str, List[str]]
MOD_NAMES: List[str]
PACKAGES: Any
PACKAGE_DATA: Dict[str, List[str]]
USE_OPENMP_DEFAULT: Optional[str]
build_ext: Any
ccompiler: module
chdir: Callable[..., contextlib._GeneratorContextManager]
contextlib: module
distutils: module
find_packages: Any
io: module
msvccompiler: module
os: module
print_function: __future__._Feature
setup: Any
subprocess: module
sys: module

class build_ext_options:
    def build_options(self) -> None: ...

class build_ext_subclass(Any, build_ext_options):
    def build_extensions(self) -> None: ...

def clean(path) -> None: ...
def generate_cython(root, source) -> None: ...
def get_python_inc(plat_specific: bool = ..., prefix: Optional[str] = ...) -> str: ...
def is_new_osx() -> bool: ...
def is_source_release(path) -> bool: ...
def setup_package() -> None: ...
