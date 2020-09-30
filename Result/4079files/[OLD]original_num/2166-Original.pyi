# (generated with --quick)

import queue
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union
import urllib.parse

API_BUSINESS: str
API_CITY: str
API_DESIGN: str
API_ENTERTAINMENT: str
API_FASHION: str
API_GAME: str
API_INTELLIGENT: str
API_LONG: str
API_URL: str
ARTICLE_ID_SET: set
ArticleDB: Any
BeautifulSoup: Any
CONFIG_QDAILY: Any
Crawler: Any
DEFAULT_HEADERS: Dict[str, Any]
DESC: Dict[str, Union[str, Dict[str, Union[bool, str, List[Dict[str, Union[bool, str]]], Tuple[bool, str]]]]]
HTML2Kindle: Any
HTML_PARSER_NAME: str
LOG: Any
Log: Any
MAIN_CONFIG: Any
META: Any
PriorityQueue: Type[queue.PriorityQueue]
Queue: Type[queue.Queue]
RetryDownload: Any
SCRIPT_CONFIG: Any
SendEmail2Kindle: Any
Task: Any
__all__: List[str]
check_config: Any
datetime: module
format_file_name: Any
format_haoqixin_content: Any
load_config: Any
make_crawler_meta: Any
md5string: Any
os: module
re: module
time: module
traceback: module
write: Any

_T = TypeVar('_T')
_T0 = TypeVar('_T0')

def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def main(start = ..., end = ..., i = ..., img = ..., gif = ..., email = ..., **kw) -> None: ...
def parser_content(task: _T0) -> Tuple[_T0, list]: ...
def parser_downloader_img(task: _T0) -> Tuple[_T0, None]: ...
def parser_list(task) -> Tuple[None, list]: ...
def qdaily_main(start, end, kw) -> None: ...
def resulter_content(task) -> None: ...
def resulter_downloader_img(task) -> None: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
