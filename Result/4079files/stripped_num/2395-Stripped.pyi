# (generated with --quick)

from typing import Any, List, Optional, Pattern, Tuple
import urllib.parse

pos_placeholders: List[str]
re: module
sys: module
wpull: Any

class Ignoracle(object):
    __doc__: str
    _compiled: List[Tuple[nothing, Pattern]]
    _primary: Optional[Tuple[Any, Any]]
    patterns: list
    def ignores(self, url_record) -> bool: ...
    def set_patterns(self, strings) -> None: ...

def parameterize_record_info(record_info) -> dict: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
