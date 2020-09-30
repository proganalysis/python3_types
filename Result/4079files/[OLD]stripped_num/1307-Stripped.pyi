# (generated with --quick)

from typing import Any, Generator, Optional, Tuple, TypeVar, Union

EXCLUDE: Tuple[str, str]
HTTPDIR: str
fnmatch: module
i: Tuple[str, str, str, str]
json: module
os: module
requests: module
time: module

AnyStr = TypeVar('AnyStr', str, bytes)

def CTimeWA(dirpath) -> Union[float, int]: ...
def genRepoList() -> Generator[Tuple[str, str, str, str], Any, None]: ...
def getOthers() -> Generator[Tuple[Any, Any], Any, None]: ...
def testHelpLink(name) -> str: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
