# (generated with --quick)

import collections
import types
from typing import Any, List, Type

LambdaType: Type[types.FunctionType]
OrderedDict: Type[collections.OrderedDict]
__all__: List[str]
flip: Any
juxt: Any
map: Any
partial: Any
pipe: Any
valmap: Any

class Condictional(collections.OrderedDict):
    __doc__: str
    key: Any
    def __call__(self, *args, **kwargs) -> Any: ...
    def __init__(self, args = ..., default = ..., key = ...) -> None: ...
    def default(self) -> Any: ...

class DictCallable(dict):
    def __call__(self, *args, **kwargs) -> Any: ...

class Dispatch(Condictional):
    __doc__: str
    default: Any
    def __init__(self, args = ..., default = ...) -> None: ...
    def key(self, key, *args, **kwargs) -> bool: ...

class ListCallable(list):
    def __call__(self, *args, **kwargs) -> list: ...

class SetCallable(set):
    def __call__(self, *args, **kwargs) -> Any: ...

class TupleCallable(tuple):
    def __call__(self, *args, **kwargs) -> Any: ...
