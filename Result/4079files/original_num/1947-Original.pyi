# (generated with --quick)

from typing import Any, List, Optional, Pattern, Tuple, TypeVar, Union

BeautifulSoup: Any
abc: module
etree: Any
functools: module
html: module
logger: logging.Logger
logging: module
magic: Any
re: module
subprocess: module

_T1 = TypeVar('_T1')

class Accept(object):
    mime: Any
    q: Any
    def __eq__(self, other) -> Any: ...
    def __init__(self, mime, q = ...) -> None: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...

class Document:
    description: None
    encoding: None
    errors: List[nothing]
    human_readable_type: None
    mime_type: None
    override_format: None
    size: None
    title: None
    url: None
    def __init__(self) -> None: ...

class DocumentParser(metaclass=abc.ABCMeta):
    accepts: list
    def __init__(self, accepts, **kwargs) -> None: ...
    @abstractmethod
    def fetch_metadata_into(self, metadata) -> Any: ...

class File(DocumentParser):
    accepts: List[Accept]
    file_binary: Any
    magic: Any
    def __init__(self, file_binary = ..., q = ..., **kwargs) -> None: ...
    def fetch_metadata_into(self, metadata) -> bool: ...

class HTML(DocumentParser):
    accepts: list
    charset_re: Pattern[bytes]
    description_blacklist: frozenset
    meta_re: Pattern[str]
    title_re: Pattern[str]
    xhtml_meta: str
    xhtml_ns: str
    xhtml_title: str
    def __init__(self, accepts = ..., description_blacklist = ..., **kwargs) -> None: ...
    def _parse_heuristic(self, contents) -> Tuple[Optional[str], str]: ...
    def _parse_html(self, tree) -> Tuple[Any, Any]: ...
    def _parse_xhtml(self, tree) -> Tuple[Any, Any]: ...
    @classmethod
    def detect_encoding(cls, buf) -> Any: ...
    def fetch_metadata_into(self, metadata) -> bool: ...

class PlainText(DocumentParser):
    __doc__: str
    accepts: List[Accept]
    max_excerpt_length: Any
    def __init__(self, max_excerpt_length = ..., q = ...) -> None: ...
    def fetch_metadata_into(self, metadata) -> bool: ...

def guess_encoding(buf, authorative: _T1 = ...) -> Tuple[Any, Union[str, _T1]]: ...
