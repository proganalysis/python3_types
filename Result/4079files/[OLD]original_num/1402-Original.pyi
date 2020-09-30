# (generated with --quick)

import queue
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union
import urllib.parse

ARTICLE_ID_SET: set
ArticleDB: Any
BeautifulSoup: Any
CONFIG_ZHIHU_ZHUANLAN: Any
Crawler: Any
DEFAULT_HEADERS: Dict[str, Any]
DESC: Dict[str, Union[str, Dict[str, Union[bool, str, List[Dict[str, Union[bool, str]]], Tuple[bool, str]]]]]
HTML2Kindle: Any
HTML_PARSER_NAME: str
INF: Any
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
format_zhihu_content: Any
load_config: Any
make_crawler_meta: Any
md5string: Any
os: module
re: module
read_file_to_list: Any
time: module
write: Any

_T = TypeVar('_T')
_T0 = TypeVar('_T0')

def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def main(i, f = ..., start = ..., end = ..., img = ..., gif = ..., email = ..., **kw) -> None: ...
def parser_content(task: _T0) -> Tuple[_T0, list]: ...
def parser_downloader_img(task: _T0) -> Tuple[_T0, None]: ...
def parser_list(task) -> Tuple[None, list]: ...
def resulter_content(task) -> None: ...
def resulter_downloader_img(task) -> None: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
def zhihu_zhuanlan_main(zhuanlan_name_list, start, end, kw) -> None: ...
