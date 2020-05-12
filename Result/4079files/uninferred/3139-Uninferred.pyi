from distutils.command import build_ext
from typing import Any

source: Any
required: Any
long_description: Any
requires_optimization: Any
ext_modules: Any

class BuildFailed(Exception): ...

class AllowFailRepair(build_ext.build_ext):
    def run(self) -> None: ...
    def build_extension(self, ext: Any) -> None: ...

def get_simple_vars_from_src(src: Any): ...

variables: Any
classifiers: Any
keywords: Any
setup_args: Any
