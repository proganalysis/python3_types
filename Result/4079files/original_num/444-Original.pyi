# (generated with --quick)

from typing import AbstractSet, Any, Coroutine, Optional, Tuple

abc: module
aiohttp: Any
enum: module
http: module
web: Any

class CLAHost(abc.ABC):
    __doc__: str
    @abstractmethod
    def check(self, client, usernames: AbstractSet[str]) -> Coroutine[Any, Any, Status]: ...

class ContribHost(abc.ABC):
    __doc__: str
    route: Tuple[str, str]
    @classmethod
    @abstractmethod
    def process(cls, server: ServerHost, request, client) -> Coroutine[Any, Any, ContribHost]: ...
    @abstractmethod
    def update(self, status: Status) -> Coroutine[Any, Any, None]: ...
    @abstractmethod
    def usernames(self) -> Coroutine[Any, Any, AbstractSet[str]]: ...

class ResponseExit(Exception):
    __doc__: str
    response: Any
    def __init__(self, *args, status: http.HTTPStatus, text: Optional[str] = ...) -> None: ...

class ServerHost(abc.ABC):
    __doc__: str
    @abstractmethod
    def contrib_auth_token(self) -> str: ...
    @abstractmethod
    def contrib_secret(self) -> str: ...
    @abstractmethod
    def log(self, message: str) -> None: ...
    @abstractmethod
    def log_exception(self, exc: BaseException) -> None: ...
    @abstractmethod
    def port(self) -> int: ...
    @abstractmethod
    def trusted_users(self) -> AbstractSet[str]: ...
    @abstractmethod
    def user_agent(self) -> Optional[str]: ...

class Status(enum.Enum):
    __doc__: str
    not_signed: int
    signed: int
    username_not_found: int
