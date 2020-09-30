# (generated with --quick)

import requests.sessions
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Tuple, TypeVar, Union

logger: logging.Logger
logging: module
requests: module
uuid: module

AnyStr = TypeVar('AnyStr', str, bytes)

class Authentication(object):
    __doc__: str
    def get_session(self) -> requests.sessions.Session: ...
    def is_ready(self) -> bool: ...

class OAuthAuthentication(Authentication):
    OAuthError: type
    __doc__: str
    auth_url: str
    base_url: str
    client_id: str
    client_secret: str
    real_auth: TokenAuthentication
    redirect_url: str
    token_url: str
    def __init__(self, redirect_url: str, client_id: str, client_secret: str, auth_token: str = ...) -> None: ...
    @staticmethod
    def _generate_state() -> str: ...
    def authorize_url(self, scope: list, state: Optional[str] = ...) -> tuple: ...
    def obtain_token(self, redirect_url: str, state: str) -> str: ...

class TokenAuthentication(Authentication):
    __doc__: str
    auth_token: str
    def __init__(self, auth_token: str = ...) -> None: ...
    def set_token(self, auth_token: str) -> None: ...

def parse_qs(qs: Optional[AnyStr], keep_blank_values: bool = ..., strict_parsing: bool = ..., encoding: str = ..., errors: str = ...) -> Dict[AnyStr, List[AnyStr]]: ...
def urlencode(query: Union[Mapping, Sequence[Tuple[Any, Any]]], doseq: bool = ..., safe: AnyStr = ..., encoding: str = ..., errors: str = ..., quote_via: Callable[[str, AnyStr, str, str], str] = ...) -> str: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
