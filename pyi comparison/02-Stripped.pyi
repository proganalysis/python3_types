# (generated with --quick)

import abc
from typing import Any, Callable, List, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
__all__: List[str]
e: Any
log: Logging
sys: module
time: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class ConsoleLogging(Logging):
    __doc__: str
    def error(self, *objs, flush = ...) -> None: ...
    def message(self, *objs, flush = ...) -> None: ...
    def warning(self, *objs, flush = ...) -> None: ...

class FileLogging(ConsoleLogging):
    __doc__: str
    def __init__(self) -> None: ...

class Logging(metaclass=abc.ABCMeta):
    __doc__: str
    _current_time: str
    @abstractmethod
    def error(self) -> Any: ...
    @abstractmethod
    def message(self) -> Any: ...
    @abstractmethod
    def warning(self) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
