# (generated with --quick)

import configparser
import html.parser
from typing import Any, Dict, List, Tuple, Type

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
    err: Any
    errors: int
    last_err_pos: int
    link_parseable_types: List[str]
    link_procs: Any
    link_types: Dict[str, Tuple[str, List[str]]]
    message: Any
    ok: bool
    def __getstate__(self) -> Dict[str, int]: ...
    def __init__(self, message, link_procs, err = ...) -> None: ...
    def error(self, message) -> None: ...
    def feed(self, chunk) -> None: ...
    def handle_starttag(self, tag, attrs) -> None: ...

def show_link(base, link, tag, title) -> None: ...
