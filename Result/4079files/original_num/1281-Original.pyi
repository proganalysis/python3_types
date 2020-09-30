# (generated with --quick)

from typing import Any, Type
import werkzeug.datastructures

ImmutableDict: Type[werkzeug.datastructures.ImmutableDict]
errno: module
os: module
typechecked: Any
types: module

class Config(dict):
    __init__: Any
    from_envvar: Any
    from_object: Any
    from_pyfile: Any
    get_namespace: Any

class ConfigAttribute(object):
    __doc__: str
    def __get__(self, obj: object, type_ = ...) -> Any: ...
    def __init__(self, name: str, get_converter = ...) -> None: ...
    def __set__(self, obj: object, value: object) -> None: ...
    def get_converter(self, _1) -> Any: ...

def import_string(import_name, silent: bool = ...) -> Any: ...
