# (generated with --quick)

import collections
from typing import Any, Type

OrderedDict: Type[collections.OrderedDict]
camelcase_to_underscores: Any
inspect: module

class HubEntityMetaClass(type):
    __doc__: str
    def __new__(mcs: Type[HubEntityMetaClass], name, bases, classdict) -> Any: ...

class LinkEntityMetaClass(type):
    def __new__(mcs: Type[LinkEntityMetaClass], name, bases, classdict) -> Any: ...

class OrderedTableMetaClass(type):
    __doc__: str
    def __new__(mcs: Type[OrderedTableMetaClass], name, bases, classdict) -> Any: ...
    @classmethod
    def __prepare__(mcs, name, bases) -> collections.OrderedDict[nothing, nothing]: ...

def __getattr__(name) -> Any: ...
