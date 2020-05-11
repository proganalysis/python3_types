# (generated with --quick)

from typing import Any, Dict, Generator, IO, Optional, Set, Type, TypeVar, Union

CACHE_REFRESH: int
COMMAND_TEMPLATE: str
ElementTree: module
HISTORY_TEMPLATE: str
PORT: int
PROTOCOL: str
QUERY: str
REQUEST_TEMPLATE: str
SERVER: str
__version__: str
asyncio: module
atexit: module
datetime: Type[datetime.datetime]
dugong: Any
executable: str
features: Dict[int, Dict[str, Optional[Union[int, str, Set[Optional[str]]]]]]
featuresTime: float
getData: Any
getDataMinimal: Any
gzip: module
hug: Any
json: module
shlex: module
shutil: module
sqlite3: module
ssl: module
subprocess: module
time: module
urllib: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T0 = TypeVar('_T0')

@overload
def NamedTemp(mode, buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[str]: ...
@overload
def NamedTemp(mode = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO[bytes]: ...
@overload
def NamedTemp(mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., delete: bool = ...) -> IO: ...
def chunks(l, n) -> Generator[Any, Any, None]: ...
def generateHeaders(referer: _T0) -> Dict[str, Union[str, _T0]]: ...
def pipeline(hostname, port, path_list, headers = ...) -> Any: ...
def set_default(obj) -> list: ...
