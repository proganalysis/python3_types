# (generated with --quick)

import requests.auth
from typing import Any, Tuple, Type, TypeVar

AuthBase: Type[requests.auth.AuthBase]

_T0 = TypeVar('_T0')

class SessionAuthentication(requests.auth.AuthBase):
    __doc__: str
    csrf_cookie_name: Any
    csrf_header_name: Any
    csrf_token: Any
    safe_methods: Tuple[str, str, str, str]
    def __call__(self, request: _T0) -> _T0: ...
    def __init__(self, csrf_cookie_name = ..., csrf_header_name = ...) -> None: ...
    def store_csrf_token(self, response, **kwargs) -> None: ...

class TokenAuthentication(requests.auth.AuthBase):
    scheme: Any
    token: Any
    def __call__(self, request: _T0) -> _T0: ...
    def __init__(self, token, scheme = ...) -> None: ...
