from setuptools.command.test import test as TestCommand
from typing import Any

class PyTest(TestCommand):
    user_options: Any = ...
    pytest_args: str = ...
    def initialize_options(self) -> None: ...
    def run_tests(self) -> None: ...

def open_local(paths: Any, mode: str = ..., encoding: str = ...): ...

version: Any
long_description: Any
setup_kwargs: Any
env_dependency: str
ujson: Any
uvloop: Any
requirements: Any
tests_require: Any
extras_require: Any
