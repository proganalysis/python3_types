# (generated with --quick)

from typing import List, NoReturn, TypeVar

shutil: module
subprocess: module

AnyStr = TypeVar('AnyStr', str, bytes)

def die(message) -> NoReturn: ...
def ensure_shellcheck_installed() -> None: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def green(message) -> None: ...
def main() -> None: ...
def run_shellcheck() -> None: ...
