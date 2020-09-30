# (generated with --quick)

from typing import Any, List, NoReturn, TextIO, Tuple

TestCommand: Any
f: TextIO
find_packages: Any
long_description: str
os: module
readme: str
requirements: List[str]
setup: Any
sys: module

class PyTest(Any):
    pytest_args: List[nothing]
    test_args: List[nothing]
    test_suite: bool
    user_options: List[Tuple[str, str, str]]
    def finalize_options(self) -> None: ...
    def initialize_options(self) -> None: ...
    def run_tests(self) -> NoReturn: ...
