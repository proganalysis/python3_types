# (generated with --quick)

import requests.auth
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Tuple, Type, TypeVar, Union
import urllib.parse

HTTPBasicAuth: Type[requests.auth.HTTPBasicAuth]
requests: module
time: module

AnyStr = TypeVar('AnyStr', str, bytes)

class OAuth:
    AUTHORIZE_URL: str
    TOKEN_URL: str
    _token: None
    authorize_url: str
    auto_refresh: Any
    client_id: Any
    client_secret: Any
    redirect_uri: Any
    scopes: Any
    session: Any
    state: Any
    token: Any
    def __init__(self, client_id, client_secret, redirect_uri = ..., scopes = ..., state = ..., auto_refresh = ..., requests = ...) -> None: ...
    def parse_response_code(self, url) -> Any: ...
    def refresh_token(self) -> None: ...
    def refresh_token_if_needed(self, expires_in = ...) -> None: ...
    def request_client_credentials(self) -> None: ...
    def request_token(self, url_or_code) -> None: ...

def parse_qs(qs: Optional[AnyStr], keep_blank_values: bool = ..., strict_parsing: bool = ..., encoding: str = ..., errors: str = ...) -> Dict[AnyStr, List[AnyStr]]: ...
def urlencode(query: Union[Mapping, Sequence[Tuple[Any, Any]]], doseq: bool = ..., safe: AnyStr = ..., encoding: str = ..., errors: str = ..., quote_via: Callable[[str, AnyStr, str, str], str] = ...) -> str: ...
@overload
def urlsplit(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResult: ...
@overload
def urlsplit(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResultBytes: ...
