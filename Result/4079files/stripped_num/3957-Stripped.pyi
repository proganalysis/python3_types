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
    dsl_impl: Any
    expr: Any
    def Base(self: DSLContract[nothing]) -> DSLContract[nothing]: ...
    def __init__(self: DSLContract[nothing], dsl_impl, expr = ...) -> None: ...
    def append_tree(self: DSLContract[nothing], expr) -> DSLContract[nothing]: ...

class DSLImplementation(abc.ABC):
    __doc__: str
    @abstractmethod
    def base_delegate(self) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
