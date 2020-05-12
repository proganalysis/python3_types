# (generated with --quick)

import _importlib_modulespec
import abc
from typing import Any, Callable, Optional, Type, TypeVar

ABC: Type[abc.ABC]
Circuit: Any
SolverError: Any
log: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class PostSolver(abc.ABC):
    @staticmethod
    def build(postsolver_name) -> Any: ...
    @abstractmethod
    def post_solve(self, circuit) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
def import_module(name: str, package: Optional[str] = ...) -> _importlib_modulespec.ModuleType: ...
