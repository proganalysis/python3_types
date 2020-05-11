# (generated with --quick)

import abc
from typing import Any, Callable, Dict, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
ddns: Any
logger: logging.Logger
logging: module
platform: module
requests: module
urllib: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class Base3FactsHTTPUpdater(BaseHTTPUpdater):
    _hostname: None
    _password: None
    _username: None
    def __init__(self, hostname, username, password, *args, **kwargs) -> None: ...
    def build_payload(self) -> Any: ...

class BaseHTTPUpdater(BaseUpdater):
    _api_url: Any
    _data: Dict[nothing, nothing]
    _headers: Dict[str, str]
    _query: Dict[nothing, nothing]
    def __int__(self, *args, **kwargs) -> None: ...
    def updater(self) -> Any: ...

class BaseUpdater(metaclass=abc.ABCMeta):
    _externalIp: None
    _useragent: str
    @abstractmethod
    def build_payload(self) -> Any: ...
    @classmethod
    def get_external_ip(self) -> None: ...
    @abstractmethod
    def parse_result(self, response) -> Any: ...
    @abstractmethod
    def updater(self) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
