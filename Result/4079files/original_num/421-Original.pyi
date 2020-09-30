# (generated with --quick)

from typing import Any, NoReturn

AnimatedProgress: Any
C: Any
Frames: Any
NAME: str
SCRIPT: str
SCRIPTDIR: str
USAGESTR: str
VERSION: str
VERSIONSTR: str
_build_rainbow_variants: Any
colr_auto_disable: Any
colr_version: Any
docopt: Any
ex: ImportError
os: module
subprocess: module
sys: module

class InvalidArg(ValueError):
    __doc__: str
    msg: Any
    def __init__(self, msg = ...) -> None: ...

def entry_point() -> NoReturn: ...
def list_frames() -> int: ...
def main(argd) -> int: ...
def print_err(*args, **kwargs) -> None: ...
def run_cmd(args, msg = ..., frameset = ..., append = ..., stderr = ...) -> int: ...
