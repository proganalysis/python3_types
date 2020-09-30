# (generated with --quick)

import __future__
from typing import Any, Dict, Generator, List, Optional, Tuple, Union

BASEDIR: str
CFUNITS_DIR: str
COMPILER_DIRECTIVES: Dict[str, bool]
Command: Any
DEFINE_MACROS: Optional[List[Tuple[str, str]]]
Extension: Any
FLAG_COVERAGE: str
NAME: str
absolute_import: __future__._Feature
cmdclass: dict
cythonize: Any
description: str
division: __future__._Feature
ext: str
extra_extension_args: dict
find_packages: Any
include_dir: Optional[Union[int, str]]
include_dirs: List[Union[int, str]]
library_dir: Optional[Union[int, str]]
library_dirs: List[Union[int, str]]
os: module
print_function: __future__._Feature
setup: Any
sys: module
udunits_ext: Any
versioneer: Any

class CleanCython(Any):
    description: str
    user_options: List[nothing]
    def finalize_options(self) -> None: ...
    def initialize_options(self) -> None: ...
    def run(self) -> None: ...

def file_walk_relative(top, remove = ...) -> Generator[Any, Any, None]: ...
def get_config_var(name: str) -> Optional[Union[int, str]]: ...
def load(fname) -> List[str]: ...
def long_description() -> str: ...
def numpy_build_ext(pars) -> Any: ...
