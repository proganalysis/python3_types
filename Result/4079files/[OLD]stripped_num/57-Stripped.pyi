# (generated with --quick)

import abc
import types
from typing import Any, Callable, Dict, Set, Tuple, Type, TypeVar, Union

ABCMeta: Type[abc.ABCMeta]
MethodType: Type[types.MethodType]
QtCore: Any
_: Any
from_utf8: Any
re: module
showWarning: Any
wrap: Any

_FuncT = TypeVar('_FuncT', bound=Callable)
_T0 = TypeVar('_T0')
_T2 = TypeVar('_T2')

class AbstractRegisteringType(abc.ABCMeta):
    members: Set[AbstractRegisteringType]
    def __init__(cls: AbstractRegisteringType, name, bases, attributes) -> None: ...

class MenuAction(SnakeNameMixin, metaclass=AbstractRegisteringType):
    app: Any
    checkable: bool
    is_checked: bool
    label: Any
    members: Set[Type[MenuAction]]
    shortcut: None
    def __init__(self, app) -> None: ...
    @abstractmethod
    def action(self) -> Any: ...

class PropertyDescriptor:
    value: Any
    def __get__(self, obj, obj_type) -> Any: ...
    def __init__(self, value = ...) -> None: ...
    def __set__(self, obj, value) -> None: ...

class RequiringMixin:
    dependencies: Dict[nothing, nothing]
    require: Set[nothing]
    def __getattr__(self, attr) -> None: ...
    def __init__(self, app) -> None: ...

class Setting(RequiringMixin, SnakeNameMixin, metaclass=SingletonMetaclass):
    app: Any
    default_value: Any
    instance: Any
    members: Set[Type[Setting]]
    value: Any
    def __new__(cls, *args, **kwargs) -> Any: ...
    def on_load(self) -> None: ...
    def on_save(self) -> None: ...
    def reset(self) -> None: ...

class SingletonMetaclass(AbstractRegisteringType):
    __new__: Callable
    instance: None
    members: Set[SingletonMetaclass]
    def __init__(cls: SingletonMetaclass, name, bases, attributes) -> None: ...

class SnakeNameMixin:
    name: str

class StylerMetaclass(AbstractRegisteringType):
    __doc__: str
    __new__: Callable
    additions: dict
    instance: None
    members: Set[StylerMetaclass]
    replacements: dict
    def __init__(cls: StylerMetaclass, name, bases, attributes) -> None: ...

class appends_in_night_mode(PropertyDescriptor):
    appends_in_night_mode: bool
    value: Any

class css(PropertyDescriptor):
    is_css: bool
    value: Any

class replaces_in_night_mode(PropertyDescriptor):
    replaces_in_night_mode: bool
    value: Any

def abstract_property(func) -> property: ...
def abstractmethod(callable: _FuncT) -> _FuncT: ...
def alert(info) -> None: ...
def decorate_or_call(operator) -> Callable[[Any], Any]: ...
def isclass(object: object) -> bool: ...
def move_args_to_kwargs(original_function, args, kwargs: _T2) -> Tuple[list, _T2]: ...
def percent_escaped(method_or_value) -> Any: ...
def singleton_creator(old_creator) -> Callable: ...
def snake_case(camel_case) -> str: ...
def style_tag(method_or_value) -> Union[str, Callable]: ...
def wraps(method: _T0 = ..., position = ...) -> Union[Callable[[Any], Any], _T0]: ...
