# (generated with --quick)

import requests.auth
import requests.models
from typing import Any, Optional, Type, TypeVar

AuthBase: Type[requests.auth.AuthBase]
BinaryIO: Any
IO: Any
requests: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T0 = TypeVar('_T0')

class AptlyAPIException(Exception):
    status_code: Any
    def __init__(self, *args, status_code = ...) -> None: ...

class BaseAPIClient:
    base_url: Any
    exc_class: Type[AptlyAPIException]
    http_auth: Any
    ssl_cert: Any
    ssl_verify: Any
    timeout: Any
    def __init__(self, base_url, ssl_verify = ..., ssl_cert = ..., http_auth = ..., timeout = ...) -> None: ...
    def _error_from_response(self, resp) -> str: ...
    def _make_url(self, path: _T0) -> Any: ...
    def do_delete(self, urlpath, params = ..., data = ..., json = ...) -> requests.models.Response: ...
    def do_get(self, urlpath, params = ...) -> requests.models.Response: ...
    def do_post(self, urlpath, data = ..., params = ..., files = ..., json = ...) -> requests.models.Response: ...
    def do_put(self, urlpath, data = ..., files = ..., json = ...) -> requests.models.Response: ...

def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
