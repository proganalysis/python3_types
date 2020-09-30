# (generated with --quick)

from typing import Any

abc: module
aiohttp: Any
enum: module
http: module
web: Any

class CLAHost(abc.ABC):
    __doc__: str
    @abstractmethod
    def check(self, client, usernames) -> coroutine: ...

class ContribHost(abc.ABC):
    __doc__: str
    route: Any
    @classmethod
    @abstractmethod
    def process(cls, server, request, client) -> coroutine: ...
    @abstractmethod
    def update(self, status) -> coroutine: ...
    @abstractmethod
    def usernames(self) -> coroutine: ...

class ResponseExit(Exception):
    __doc__: str
    response: Any
    def __init__(self, *args, status, text = ...) -> None: ...

class ServerHost(abc.ABC):
    __doc__: str
    @abstractmethod
    def contrib_auth_token(self) -> Any: ...
    @abstractmethod
    def contrib_secret(self) -> Any: ...
    @abstractmethod
    def log(self, message) -> Any: ...
    @abstractmethod
    def log_exception(self, exc) -> Any: ...
    @abstractmethod
    def port(self) -> Any: ...
    @abstractmethod
    def trusted_users(self) -> Any: ...
    @abstractmethod
    def user_agent(self) -> Any: ...

class Status(enum.Enum):
    __doc__: str
    not_signed: int
    signed: int
    username_not_found: int
