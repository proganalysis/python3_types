# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar

ABC: Type[abc.ABC]
User: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class UserSource(abc.ABC):
    __doc__: str
    def add_user(self, user) -> None: ...
    def get_all_users(self) -> list: ...
    @abstractmethod
    def get_user_by_identifier(self, identifier: int) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
