# (generated with --quick)

from typing import Any, Dict, List, NoReturn, Tuple

TestCommand: Any
codecs: module
env_dependency: str
extras_require: Dict[str, List[str]]
fp: codecs.StreamReaderWriter
long_description: str
os: module
re: module
requirements: List[str]
rm: codecs.StreamReaderWriter
setup: Any
setup_kwargs: Dict[str, Any]
sys: module
tests_require: List[str]
ujson: str
uvloop: str
version: Any

class PyTest(Any):
    __doc__: str
    pytest_args: str
    user_options: List[Tuple[str, str, str]]
    def initialize_options(self) -> None: ...
    def run_tests(self) -> NoReturn: ...

def open_local(paths, mode = ..., encoding = ...) -> codecs.StreamReaderWriter: ...
def strtobool(val: str) -> bool: ...
