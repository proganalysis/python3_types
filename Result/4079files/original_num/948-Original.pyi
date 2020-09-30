# (generated with --quick)

import collections
from typing import Any, Callable, Generator, Tuple, Type

APPLE_REF_TEMPLATE: str
BeautifulSoup: Any
abc: module
attr: module
click: module
codecs: module
defaultdict: Type[collections.defaultdict]
errno: module
log: logging.Logger
logging: module
os: module

class IParser(metaclass=abc.ABCMeta):
    __doc__: str
    doc_path: str
    name: str
    def detect(path: str) -> bool: ...
    def find_and_patch_entry(soup, entry: TOCEntry) -> None: ...
    def parse() -> None: ...

class ParserEntry:
    __doc__: str
    name: Any
    path: Any
    type: Any
    def __init__(self, name, type, path) -> None: ...
    def as_tuple(self) -> Tuple[Any, Any, Any]: ...

class TOCEntry:
    __doc__: str
    anchor: Any
    name: Any
    type: Any
    def __init__(self, name, type, anchor) -> None: ...

def coroutine(func) -> Callable: ...
def has_file_with(path, filename, content) -> bool: ...
def patch_anchors(*args, **kwargs) -> Generator[None, Any, nothing]: ...
