# (generated with --quick)

import pathlib
from typing import List, Type

CURRENT_HOOKS_VERSION: str
Path: Type[pathlib.Path]
QUIET: bool
SOLUTION_PATH: pathlib.Path
os: module
shutil: module
subprocess: module
sys: module

def install_hooks() -> None: ...
def reset_solution() -> None: ...
def run_command(command: List[str], capture: bool = ...) -> subprocess.CompletedProcess: ...
def update_submodules() -> None: ...
