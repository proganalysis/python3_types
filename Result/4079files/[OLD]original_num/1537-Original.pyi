# (generated with --quick)

import badwolf.lint
import badwolf.lint.linters
from typing import Any, Generator, List, Optional, Tuple, Type, Union

Linter: Type[badwolf.lint.linters.Linter]
Problem: Type[badwolf.lint.Problem]

class ShellCheckLinter(badwolf.lint.linters.Linter):
    default_pattern: str
    name: str
    def create_command(self, files) -> list: ...
    def lint_files(self, files) -> Generator[badwolf.lint.Problem, Any, None]: ...

def in_path(name) -> bool: ...
def parse_checkstyle(xml) -> Generator[Tuple[Optional[str], Any, Optional[str]], Any, None]: ...
def run_command(command, split = ..., include_errors = ..., cwd = ..., shell = ..., env = ...) -> Tuple[int, Union[str, List[str]]]: ...
