# (generated with --quick)

from typing import Any, Callable, List, Optional, TypeVar

DEFAULT_PREFIX: Optional[str]
DEFAULT_SUFFIX: Optional[str]
__all__: List[str]
functools: module
os: module
shutil: module
sys: module
tempfile: module
typing: module
uuid: module

_TScratchDir = TypeVar('_TScratchDir', bound=ScratchDir)

class ScratchDir:
    NamedTemporaryFile: Callable
    SpooledTemporaryFile: Callable
    TemporaryFile: Callable
    __doc__: str
    base: Any
    child: Callable
    directory: Callable
    file: Callable
    filename: Callable
    is_active: bool
    join: Callable
    mkdtemp: Callable
    mkstemp: Callable
    named: Callable
    prefix: str
    root: Any
    secure: Callable
    spooled: Callable
    suffix: str
    teardown: Callable
    wd: Any
    def __enter__(self: _TScratchDir) -> _TScratchDir: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, prefix: str = ..., suffix: str = ..., base: Optional[str] = ..., root: Optional[str] = ..., wd: Optional[str] = ...) -> None: ...
    def setup(self) -> None: ...

class ScratchDirError(Exception):
    __doc__: str

class ScratchDirInactiveError(ScratchDirError):
    __doc__: str

def requires_activation(func) -> Callable: ...
