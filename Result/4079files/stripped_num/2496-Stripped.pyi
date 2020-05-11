# (generated with --quick)

import contextlib
from typing import Any, IO, Optional, Pattern, Tuple, Type, TypeVar, Union
import zipfile

ALT_BASE_URL: Optional[str]
BASE_URL: str
FILENAME: str
JAVA_6_COMPATIBLE_VERSION: str
JAVA_7_COMPATIBLE_VERSION: str
JAVA_VERSION_REGEX: Pattern[str]
LATEST_VERSION: str
PACKAGE_PATH: str
ZipFile: Type[zipfile.ZipFile]
closing: Type[contextlib.closing]
glob: module
os: module
re: module
shutil: module
subprocess: module
sys: module
urljoin: Any
urlopen: Any

AnyStr = TypeVar('AnyStr', str, bytes)

@overload
def TemporaryFile(mode, buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ...) -> IO[str]: ...
@overload
def TemporaryFile(mode = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ...) -> IO[bytes]: ...
@overload
def TemporaryFile(mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ...) -> IO: ...
def download_lt(update = ...) -> None: ...
def find_executable(executable: str, path: Optional[str] = ...) -> Optional[str]: ...
def get_common_prefix(z) -> Any: ...
def get_newest_possible_languagetool_version() -> str: ...
def parse_java_version(version_text) -> Tuple[int, int]: ...
@overload
def warn(message: Warning, category = ..., stacklevel: int = ..., source = ...) -> None: ...
@overload
def warn(message: str, category: Optional[Type[Warning]] = ..., stacklevel: int = ..., source = ...) -> None: ...
