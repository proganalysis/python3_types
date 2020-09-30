# (generated with --quick)

import abc
from typing import Any, Callable, Generator, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]

_FuncT = TypeVar('_FuncT', bound=Callable)

class AbstractTransport(metaclass=abc.ABCMeta):
    __metaclass__: Type[abc.ABCMeta]
    app: None
    max_message_size: int
    router: None
    @abstractmethod
    def get_end_points_to_add(self) -> Any: ...
    @abstractmethod
    def get_help_message(self) -> Any: ...
    def get_reply_message(self, sender_id: str, message: str) -> Generator[str, None, None]: ...
    @abstractmethod
    def get_response(self, message) -> Any: ...
    @abstractmethod
    def send_message(self, sender_id, message) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
