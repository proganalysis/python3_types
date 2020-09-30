# (generated with --quick)

import requests.auth
import requests.models
from typing import Any, Dict, List, MutableMapping, Optional, Sequence, Tuple, Type, TypeVar, Union

AuthBase: Type[requests.auth.AuthBase]
BinaryIO: Any
IO: Any
requests: module

AnyStr = TypeVar('AnyStr', str, bytes)

class AptlyAPIException(Exception):
    status_code: int
    def __init__(self, *args, status_code: int = ...) -> None: ...

class BaseAPIClient:
    base_url: str
    exc_class: Type[AptlyAPIException]
    http_auth: Optional[requests.auth.AuthBase]
    ssl_cert: Optional[Tuple[str, str]]
    ssl_verify: Optional[Union[bool, str]]
    timeout: int
    def __init__(self, base_url: str, ssl_verify: Union[bool, str] = ..., ssl_cert: Optional[Tuple[str, str]] = ..., http_auth: Optional[requests.auth.AuthBase] = ..., timeout: int = ...) -> None: ...
    def _error_from_response(self, resp: requests.models.Response) -> str: ...
    def _make_url(self, path: str) -> str: ...
    def do_delete(self, urlpath: str, params: Optional[Dict[str, str]] = ..., data: Optional[Union[str, Dict[str, str], Sequence[Tuple[str, str]]]] = ..., json: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = ...) -> requests.models.Response: ...
    def do_get(self, urlpath: str, params: Optional[Dict[str, str]] = ...) -> requests.models.Response: ...
    def do_post(self, urlpath: str, data = ..., params: Optional[Dict[str, str]] = ..., files: Optional[Union[Dict[str, Any], Sequence[tuple]]] = ..., json: Optional[MutableMapping] = ...) -> requests.models.Response: ...
    def do_put(self, urlpath: str, data = ..., files: Optional[Union[Dict[str, Any], Sequence[tuple]]] = ..., json: Optional[MutableMapping] = ...) -> requests.models.Response: ...

def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
