# (generated with --quick)

import http.cookies
from typing import Any, Dict, List, Optional, Type, TypeVar
import wsgiref.headers

HTTP_CODES: Dict[int, str]
Headers: Type[wsgiref.headers.Headers]
SimpleCookie: Type[http.cookies.SimpleCookie]
_HTTP_STATUS_LINES: Dict[int, str]
base64: module
hashlib: module
hmac: module
http_client: module
json: module
pickle: module
request: Any
time: module

AnyStr = TypeVar('AnyStr', str, bytes)

class BaseResponse:
    __doc__: str
    _body: Any
    _cookies: http.cookies.SimpleCookie[nothing]
    _status_code: Any
    body: Any
    default_content_type: str
    default_status: int
    headerlist: Any
    headers: wsgiref.headers.Headers
    status: str
    status_code: Any
    def __init__(self, body = ..., status = ..., headers = ...) -> None: ...
    def delete_cookie(self, key, **kwargs) -> None: ...
    def set_cookie(self, key, value, expires = ..., max_age = ..., path = ..., secret = ..., digestmod = ...) -> None: ...

class HTTPError(Response, Exception):
    __doc__: str
    _body: list
    _cookies: http.cookies.SimpleCookie[nothing]
    _status_code: Any
    charset: Any
    default_status: int
    headers: wsgiref.headers.Headers
    def __init__(self, body, status, headers = ..., charset = ...) -> None: ...

class JSONResponse(BaseResponse):
    __doc__: str
    _body: List[bytes]
    _cookies: http.cookies.SimpleCookie[nothing]
    _status_code: Any
    default_content_type: str
    headers: wsgiref.headers.Headers
    def __init__(self, dic, status = ..., headers = ..., charset = ..., **dump_args) -> None: ...

class RedirectResponse(BaseResponse):
    __doc__: str
    _body: List[bytes]
    _cookies: http.cookies.SimpleCookie[nothing]
    _status_code: int
    headers: wsgiref.headers.Headers
    def __init__(self, url) -> None: ...

class Response(BaseResponse):
    __doc__: str
    _body: list
    _cookies: http.cookies.SimpleCookie[nothing]
    _status_code: Any
    charset: Any
    default_content_type: str
    headers: wsgiref.headers.Headers
    def __init__(self, body = ..., status = ..., headers = ..., charset = ...) -> None: ...

class TemplateResponse(BaseResponse):
    __doc__: str
    _body: list
    _cookies: http.cookies.SimpleCookie[nothing]
    _status_code: Any
    default_content_type: str
    headers: wsgiref.headers.Headers
    def __init__(self, filename, status = ..., headers = ..., charset = ..., **tpl_args) -> None: ...

def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
