# (generated with --quick)

import collections
from typing import Any, List, Tuple, Type

OrderedDict: Type[collections.OrderedDict]
_undefined: Any
rlz: Any
unique: Any
util: Any

class Annotable(metaclass=AnnotableMeta):
    __slots__ = []
    argnames: Any
    args: tuple
    def __init__(self, *args, **kwargs) -> None: ...
    def _validate(self) -> None: ...

class AnnotableMeta(type):
    def __new__(meta: Type[AnnotableMeta], name, bases, dct) -> Any: ...
    @classmethod
    def __prepare__(metacls, name, bases, **kwds) -> collections.OrderedDict[nothing, nothing]: ...

class Argument:
    __slots__ = ["default", "show", "validator"]
    __doc__: str
    default: Any
    optional: bool
    show: Any
    validator: Any
    def __call__(self, value = ..., name = ...) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __init__(self, validator, default = ..., show = ...) -> None: ...
    def validate(self, value = ..., name = ...) -> Any: ...

class TypeSignature(collections.OrderedDict):
    __slots__ = []
    def __call__(self, *args, **kwargs) -> List[Tuple[Any, Any]]: ...
    @classmethod
    def from_dtypes(cls, dtypes) -> Any: ...
    def names(self) -> Tuple[nothing, ...]: ...
    def validate(self, *args, **kwargs) -> List[Tuple[Any, Any]]: ...
