# (generated with --quick)

import abc
from typing import Any, Callable, Coroutine, Optional, Tuple, Type, TypeVar

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

class AuthorizationCodeSession(TokenSession):
    CODE_URL: str
    __doc__: str
    access_token: Any
    app_id: int
    app_secret: str
    code: str
    driver: Any
    redirect_uri: str
    timeout: int
    def __init__(self, app_id: int, app_secret: str, redirect_uri: str, code: str, timeout: int = ..., driver = ...) -> None: ...
    def authorize(self, code: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...
    def get_code(self, code: Optional[str] = ...) -> Coroutine[Any, Any, str]: ...

class BaseSession(abc.ABC):
    __doc__: str
    @abstractmethod
    def __aenter__(self) -> coroutine: ...
    def __aexit__(self, exc_type, exc_val, exc_tb) -> Coroutine[Any, Any, None]: ...
    def close(self) -> Coroutine[Any, Any, None]: ...
    @abstractmethod
    def send_api_request(self, method_name: str, params: Optional[dict] = ..., timeout: Optional[int] = ...) -> Coroutine[Any, Any, dict]: ...

class ImplicitSession(TokenSession):
    AUTH_URL: str
    __doc__: str
    access_token: Any
    app_id: int
    driver: Any
    login: str
    num_of_attempts: int
    password: str
    scope: Optional[str]
    timeout: int
    def __init__(self, login: str, password: str, app_id: int, scope: Optional[str] = ..., timeout: int = ..., num_of_attempts: int = ..., driver = ...) -> None: ...
    def _get_auth_page(self) -> Coroutine[Any, Any, str]: ...
    def _process_2auth_form(self, html: str) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def _process_access_form(self, html: str) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def _process_auth_form(self, html: str) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def enter_confirmation_code(self) -> Coroutine[Any, Any, str]: ...

class TokenSession(BaseSession):
    API_VERSION: str
    REQUEST_URL: str
    __doc__: str
    access_token: Optional[str]
    driver: Any
    timeout: int
    def __aenter__(self) -> Coroutine[Any, Any, BaseSession]: ...
    def __aexit__(self, exc_type, exc_val, exc_tb) -> coroutine: ...
    def __init__(self, access_token: Optional[str] = ..., timeout: int = ..., driver = ...) -> None: ...
    def authorize(self) -> Coroutine[Any, Any, None]: ...
    def enter_captcha(self, url: str, sid: str) -> Coroutine[Any, Any, str]: ...
    def send_api_request(self, method_name: str, params: Optional[dict] = ..., timeout: Optional[int] = ...) -> Coroutine[Any, Any, dict]: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
