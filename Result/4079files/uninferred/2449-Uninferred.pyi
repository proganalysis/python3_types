from setuptools import Command
from typing import Any

COMPILER_DIRECTIVES: Any
DEFINE_MACROS: Any
FLAG_COVERAGE: str
BASEDIR: Any
NAME: str
CFUNITS_DIR: Any

class CleanCython(Command):
    description: str = ...
    user_options: Any = ...
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

def file_walk_relative(top: Any, remove: str = ...) -> None: ...
def load(fname: Any): ...
def long_description(): ...

include_dir: Any
include_dirs: Any
library_dir: Any
library_dirs: Any
extra_extension_args: Any
ext: Any

def numpy_build_ext(pars: Any): ...

udunits_ext: Any
cmdclass: Any
description: str
