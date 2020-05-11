# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
dateutil: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class DataProvider(metaclass=abc.ABCMeta):
    __doc__: str
    @staticmethod
    def calc_delay(planned: str, actual: str) -> str: ...
    @abstractmethod
    def get(self) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
