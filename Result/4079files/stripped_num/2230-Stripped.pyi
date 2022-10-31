# (generated with --quick)

from typing import Any, Iterable, List, NoReturn, Optional

PATH_REPO: str
__all__: List[str]
os: module
subprocess: module
sys: module

def cprint(text: str, color: Optional[str] = ..., on_color: Optional[str] = ..., attrs: Optional[Iterable[str]] = ..., **kwargs) -> None: ...
def failed(string) -> NoReturn: ...
def path_repo() -> str: ...
def run(command) -> Any: ...
def run_pipe(command) -> subprocess.CompletedProcess: ...