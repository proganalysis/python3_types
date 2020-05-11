# (generated with --quick)

from typing import Any, Generator, List, Tuple

Warning: Any
helpers: Any
isolated_jedi_cache: Any
jedi: Any
os: module
pytest: Any
re: module
refactor: Any
run: Any
settings: Any

class StaticAnalysisCase(object):
    __doc__: str
    _path: Any
    _source: str
    skip: Any
    def __init__(self, path) -> None: ...
    def collect_comparison(self) -> List[Tuple[int, int, str]]: ...
    def run(self, compare_cb) -> None: ...

def collect_static_analysis_tests(base_dir, test_files) -> Generator[StaticAnalysisCase, Any, None]: ...
def parse_test_files_option(opt) -> Tuple[str, List[int]]: ...
def pytest_addoption(parser) -> None: ...
def pytest_generate_tests(metafunc) -> None: ...
