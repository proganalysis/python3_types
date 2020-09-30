# (generated with --quick)

from typing import Any, List, NoReturn, Tuple

TestCommand: Any
os: module
re: module
setup: Any
version: str

class PyTest(Any):
    pytest_args: List[nothing]
    test_args: List[nothing]
    test_suite: bool
    user_options: List[Tuple[str, str, str]]
    def finalize_options(self) -> None: ...
    def initialize_options(self) -> None: ...
    def run_tests(self) -> NoReturn: ...

def get_version(filepath) -> str: ...
