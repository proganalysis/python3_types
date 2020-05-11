# (generated with --quick)

import badwolf.lint
import badwolf.lint.linters
from typing import Any, Generator, List, Tuple, Type, Union

Problem: Type[badwolf.lint.Problem]
PythonLinter: Type[badwolf.lint.linters.PythonLinter]
logger: logging.Logger
logging: module
os: module

class MypyLinter(badwolf.lint.linters.PythonLinter):
    default_pattern: str
    name: str
    def _is_ignore_missing_imports_configured(self) -> bool: ...
    def _parse_line(self, line) -> Tuple[Any, int, Any, Any]: ...
    def lint_files(self, files) -> Generator[badwolf.lint.Problem, Any, None]: ...

def in_path(name) -> bool: ...
def run_command(command, split = ..., include_errors = ..., cwd = ..., shell = ..., env = ...) -> Tuple[int, Union[str, List[str]]]: ...
