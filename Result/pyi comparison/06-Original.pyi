# (generated with --quick)

import configparser
import html.parser
from typing import Any, Callable, Dict, List, Optional, Tuple, Type

ConfigParser: Type[configparser.ConfigParser]
HTMLParser: Type[html.parser.HTMLParser]
HttpMessage: Any
P: HTMLLinkParser
RedFetcher: Any
T: Any
chunk: Any
fetch_done: Any
headers: Any
rfc7231: Any
status: Any
sys: module
thor: Any

class BadErrorIReallyMeanIt(Exception):
    __doc__: str

class HTMLLinkParser(html.parser.HTMLParser):
    __doc__: str
    err: Optional[Callable[[str], int]]
    errors: int
    last_err_pos: int
    link_parseable_types: List[str]
    link_procs: List[Callable[[str, str, str, str], None]]
    link_types: Dict[str, Tuple[str, List[str]]]
    message: Any
    ok: bool
    def __getstate__(self) -> Dict[str, Any]: ...
    def __init__(self, message, link_procs: List[Callable[[str, str, str, str], None]], err: Optional[Callable[[str], int]] = ...) -> None: ...
    def feed(self, chunk: str) -> None: ...
    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]) -> None: ...

def show_link(base: str, link: str, tag: str, title: str) -> None: ...
