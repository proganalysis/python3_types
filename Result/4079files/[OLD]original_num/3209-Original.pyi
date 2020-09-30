# (generated with --quick)

import abc
from typing import Callable, Type, TypeVar

ABC: Type[abc.ABC]

_FuncT = TypeVar('_FuncT', bound=Callable)

class ValidatorMixin(abc.ABC):
    @abstractmethod
    def validate(self, some1, some2) -> bool: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
