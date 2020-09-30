# (generated with --quick)

import abc
from typing import Any, Callable, Coroutine, Tuple, Type, TypeVar

ABC: Type[abc.ABC]
AUTHORIZATION_FAILED: Any
AccessPageParser: Any
AuthPageParser: Any
CAPTCHA_IS_NEEDED: Any
HttpDriver: Any
TwoFactorCodePageParser: Any
URL: Any
VkAPIError: Any
VkAuthError: Any
VkCaptchaNeeded: Any
VkTwoFactorCodeNeeded: Any
json: module

_FuncT = TypeVar('_FuncT', bound=Callable)
_T0 = TypeVar('_T0')

class AuthorizationCodeSession(TokenSession):
    CODE_URL: str
    __doc__: str
    access_token: Any
    app_id: Any
    app_secret: Any
    code: Any
    driver: Any
    redirect_uri: Any
    timeout: Any
    def __init__(self, app_id, app_secret, redirect_uri, code, timeout = ..., driver = ...) -> None: ...
    def authorize(self, code = ...) -> Coroutine[Any, Any, None]: ...
    def get_code(self, code: _T0 = ...) -> coroutine: ...

class BaseSession(abc.ABC):
    __doc__: str
    @abstractmethod
    def __aenter__(self) -> coroutine: ...
    def __aexit__(self, exc_type, exc_val, exc_tb) -> Coroutine[Any, Any, None]: ...
    def close(self) -> Coroutine[Any, Any, None]: ...
    @abstractmethod
    def send_api_request(self, method_name, params = ..., timeout = ...) -> coroutine: ...

class ImplicitSession(TokenSession):
    AUTH_URL: str
    __doc__: str
    access_token: Any
    app_id: Any
    driver: Any
    login: Any
    num_of_attempts: Any
    password: Any
    scope: Any
    timeout: Any
    def __init__(self, login, password, app_id, scope = ..., timeout = ..., num_of_attempts = ..., driver = ...) -> None: ...
    def _get_auth_page(self) -> coroutine: ...
    def _process_2auth_form(self, html) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def _process_access_form(self, html) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def _process_auth_form(self, html) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def authorize(self) -> Coroutine[Any, Any, None]: ...
    def enter_confirmation_code(self) -> Coroutine[Any, Any, nothing]: ...

class TokenSession(BaseSession):
    API_VERSION: str
    REQUEST_URL: str
    __doc__: str
    access_token: Any
    driver: Any
    timeout: Any
    def __aenter__(self) -> Coroutine[Any, Any, TokenSession]: ...
    def __aexit__(self, exc_type, exc_val, exc_tb) -> coroutine: ...
    def __init__(self, access_token = ..., timeout = ..., driver = ...) -> None: ...
    def authorize(self) -> Coroutine[Any, Any, nothing]: ...
    def enter_captcha(self, url, sid) -> Coroutine[Any, Any, nothing]: ...
    def send_api_request(self, method_name, params = ..., timeout = ...) -> coroutine: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
