from setuptools.command.test import test as TestCommand
from typing import Any

here: Any
readme: Any
__version__: str
__author__: str
__author_email__: str
__license__: str
__classifiers__: Any

class PyTest(TestCommand):
    test_args: Any = ...
    test_suite: bool = ...
    def finalize_options(self) -> None: ...
    def run_tests(self) -> None: ...
