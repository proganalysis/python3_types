# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar

ABC: Type[abc.ABC]

_FuncT = TypeVar('_FuncT', bound=Callable)

class ValidatorMixin(abc.ABC):
    @abstractmethod
    def validate(self, some1, some2) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
