# (generated with --quick)

import collections
from typing import Any, Callable, Dict, Iterable, List, Sized, Tuple, Type, TypeVar

OrderedDict: Type[collections.OrderedDict]
RegisterOptions: Any
SubscribeOptions: Any
__all__: Tuple[str, str, str]
check_argument_types: Any
inspect: module

T_Options = TypeVar('T_Options')
_TProcedure = TypeVar('_TProcedure', bound=Procedure)
_TSubscriber = TypeVar('_TSubscriber', bound=Subscriber)

class Procedure(tuple):
    __slots__ = ["handler", "name", "options"]
    __dict__: collections.OrderedDict[str, Any]
    _field_defaults: collections.OrderedDict[str, Any]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str]
    handler: Callable
    name: str
    options: Any
    def __getnewargs__(self) -> Tuple[str, Callable, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TProcedure], name: str, handler: Callable, options) -> _TProcedure: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[_TProcedure], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> _TProcedure: ...
    def _replace(self: _TProcedure, **kwds) -> _TProcedure: ...

class Subscriber(tuple):
    __slots__ = ["handler", "options", "topic"]
    __dict__: collections.OrderedDict[str, Any]
    _field_defaults: collections.OrderedDict[str, Any]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str]
    handler: Callable
    options: Any
    topic: str
    def __getnewargs__(self) -> Tuple[str, Callable, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TSubscriber], topic: str, handler: Callable, options) -> _TSubscriber: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[_TSubscriber], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> _TSubscriber: ...
    def _replace(self: _TSubscriber, **kwds) -> _TSubscriber: ...

class WAMPRegistry:
    __slots__ = ["exceptions", "prefix", "procedure_defaults", "procedures", "subscription_defaults", "subscriptions"]
    __doc__: str
    exceptions: dict
    prefix: Any
    procedure_defaults: Any
    procedures: Dict[Any, Procedure]
    subscription_defaults: Any
    subscriptions: List[Subscriber]
    def __init__(self, prefix = ..., *, procedure_defaults = ..., subscription_defaults = ...) -> None: ...
    def __repr__(self, *args, **kwargs) -> str: ...
    def add_from(self, registry, prefix = ...) -> None: ...
    def add_procedure(self, handler, name = ..., options = ...) -> Procedure: ...
    def add_subscriber(self, handler, topic, options = ...) -> Subscriber: ...
    def exception(self, error) -> Callable[[Any], Any]: ...
    def map_exception(self, exc_type, code) -> None: ...
    def procedure(self, name = ..., options = ...) -> Callable: ...
    def subscriber(self, topic, options = ...) -> Callable[[Any], Any]: ...

def _apply_defaults(options, defaults) -> None: ...
def _validate_handler(handler, kind) -> None: ...
