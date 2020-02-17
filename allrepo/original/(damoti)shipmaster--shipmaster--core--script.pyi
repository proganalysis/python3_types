# (generated with --quick)

import pathlib
import tarfile
from typing import Any, IO, List, Optional, Tuple, Type, TypeVar, Union

APP_PATH: pathlib.PurePath
PurePath: Type[pathlib.PurePath]
SCRIPT_PATH: pathlib.PurePath
TarFile: Type[tarfile.TarFile]
TarInfo: Type[tarfile.TarInfo]
format_size: Any
io: module
logger: logging.Logger
logging: module
os: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T0 = TypeVar('_T0')

class Archive:
    _closed: bool
    archive: tarfile.TarFile
    archive_file: IO
    exclude: List[str]
    workspace: Any
    def __init__(self, workspace) -> None: ...
    def _filter_git(self, info: _T0) -> Optional[_T0]: ...
    def add_bundled_file(self, base, path) -> None: ...
    def add_project_file(self, path) -> None: ...
    def add_script(self, script: Script) -> None: ...
    def close(self) -> None: ...
    def getfile(self) -> IO: ...

class Script:
    _closed: bool
    info: Optional[tarfile.TarInfo]
    path: pathlib.PurePath
    source: Any
    src: io.BytesIO
    tar: Tuple[Any, Any]
    def __init__(self, name, set_dash_x = ...) -> None: ...
    def close(self) -> None: ...
    def open(self) -> None: ...
    def write(self, s = ..., newline = ...) -> None: ...
    def write_all(self, commands) -> None: ...

@overload
def NamedTemporaryFile(mode, buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[str]: ...
@overload
def NamedTemporaryFile(mode = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[bytes]: ...
@overload
def NamedTemporaryFile(mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO: ...
def fnmatch(name: AnyStr, pat: AnyStr) -> bool: ...
