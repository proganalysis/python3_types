# (generated with --quick)

from typing import Any, Callable, ContextManager, Type, TypeVar

AbstractContextManager: Type[ContextManager]
Result: Any
enum: module

E = TypeVar('E', bound=Exception)
F = TypeVar('F', bound=Exception)
T = TypeVar('T')
U = TypeVar('U')

class _ResultVariant(enum.Enum):
    ERR: enum.auto
    OK: enum.auto
    __doc__: str

def Err(error) -> Any: ...
def Ok(value) -> Any: ...
def try_(fn) -> Callable: ...
