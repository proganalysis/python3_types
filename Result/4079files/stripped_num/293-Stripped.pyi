# (generated with --quick)

import distutils.version
from typing import Any, List, Type

Extension: Any
LooseVersion: Type[distutils.version.LooseVersion]
build_ext: Any
find_packages: Any
os: module
platform: module
re: module
setup: Any
subprocess: module
sys: module

class CMakeBuild(Any):
    __doc__: str
    def build_extension(self, ext) -> None: ...
    def run(self) -> None: ...

class CMakeExtension(Any):
    __doc__: str
    sourcedir: Any
    def __init__(self, name, sourcedir = ...) -> None: ...

def requirements() -> List[str]: ...
