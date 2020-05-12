# (generated with --quick)

import __future__
from typing import Any, List, TextIO

ast: module
build_ext: module
classifiers: List[str]
collections: module
cythonize: Any
distutils: module
ext_modules: Any
f: TextIO
keywords: List[str]
long_description: str
os: module
print_function: __future__._Feature
required: List[str]
requires_optimization: list
setup_args: dict
setuptools: module
shutil: module
source: str
sys: module
variables: collections.OrderedDict[nothing, nothing]

class AllowFailRepair(Any):
    __doc__: str
    def build_extension(self, ext) -> None: ...
    def run(self) -> None: ...

class BuildFailed(Exception):
    __doc__: str

def get_simple_vars_from_src(src) -> collections.OrderedDict[nothing, nothing]: ...
