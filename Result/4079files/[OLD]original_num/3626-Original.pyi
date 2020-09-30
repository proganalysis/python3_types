# (generated with --quick)

from typing import Any, Dict, Match, Optional, Set, Type, TypeVar, Union

DEFAULT_MAX_AGE: int
_LegalChars: str
_Translator: Dict[int, str]
_UnescapedChars: str
datetime: Type[datetime.datetime]
re: module
string: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T0 = TypeVar('_T0')

class Cookie(dict):
    __doc__: str
    _flags: Set[str]
    _keys: Dict[str, str]
    key: Any
    value: Any
    def __init__(self, key, value) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def encode(self, encoding) -> bytes: ...

class CookieJar(dict):
    __doc__: str
    cookie_headers: Dict[Any, str]
    header_key: str
    headers: Any
    def __delitem__(self, key) -> Any: ...
    def __init__(self, headers) -> None: ...
    def __setitem__(self, key, value) -> None: ...

def _is_legal_key(string: AnyStr, pos: int = ..., endpos: int = ...) -> Optional[Match[AnyStr]]: ...
def _quote(str: _T0) -> Union[str, _T0]: ...
