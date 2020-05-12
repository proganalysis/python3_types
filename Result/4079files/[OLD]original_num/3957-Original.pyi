# (generated with --quick)

import abc
from typing import Any, Callable, Generic, Type, TypeVar

ABC: Type[abc.ABC]
ContextDelegate: Any
Expression: Any

DSLContractSubclass = TypeVar('DSLContractSubclass', bound=DSLContract)
DSLImplementationSubclass = TypeVar('DSLImplementationSubclass', bound=DSLImplementation)
_FuncT = TypeVar('_FuncT', bound=Callable)

class DSLContract(Generic[DSLImplementationSubclass]):
    __doc__: str
    dsl_impl: DSLImplementation
    expr: Any
    def Base(self: DSLContractSubclass) -> DSLContractSubclass: ...
    def __init__(self, dsl_impl: DSLImplementationSubclass, expr = ...) -> None: ...
    def append_tree(self: DSLContractSubclass, expr) -> DSLContractSubclass: ...

class DSLImplementation(abc.ABC):
    __doc__: str
    @abstractmethod
    def base_delegate(self) -> type: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
