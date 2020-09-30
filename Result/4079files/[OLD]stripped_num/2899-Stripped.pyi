# (generated with --quick)

import abc
import collections
import types
from typing import Any, Callable, Coroutine, IO, Optional, Tuple, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
Context: Any
OrderedDict: Type[collections.OrderedDict]
PluginContainer: Any
__all__: Tuple[str, str, str]
asyncio: module
check_argument_types: Any
component_types: Any
merge_config: Any
qualified_name: Any
sys: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class CLIApplicationComponent(ContainerComponent):
    __doc__: str
    child_components: dict
    component_configs: Any
    @abstractmethod
    def run(self, ctx) -> coroutine: ...

class Component(metaclass=abc.ABCMeta):
    __slots__ = []
    __doc__: str
    @abstractmethod
    def start(self, ctx) -> coroutine: ...

class ContainerComponent(Component):
    __slots__ = ["child_components", "component_configs"]
    __doc__: str
    child_components: dict
    component_configs: Any
    def __init__(self, components = ...) -> None: ...
    def add_component(self, alias, type = ..., **config) -> None: ...
    def start(self, ctx) -> Coroutine[Any, Any, None]: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
def print_exception(etype: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[types.TracebackType], limit: Optional[int] = ..., file: Optional[IO[str]] = ..., chain: bool = ...) -> None: ...
@overload
def warn(message: Warning, category = ..., stacklevel: int = ..., source = ...) -> None: ...
@overload
def warn(message: str, category: Optional[Type[Warning]] = ..., stacklevel: int = ..., source = ...) -> None: ...
