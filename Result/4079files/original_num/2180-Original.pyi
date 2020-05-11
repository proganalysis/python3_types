# (generated with --quick)

from typing import Any, Callable, Dict, Type

_dummy_setter: property
http: Any
patch: Any
test: Any
warnings: module

class Client(Any):
    def request(self, **request) -> Any: ...

class DataSet:
    args: tuple
    kwargs: Dict[str, Any]
    def __init__(self, *args, **kwargs) -> None: ...
    def __str__(self) -> str: ...

class Parametrized(type):
    def __new__(mcs: Type[Parametrized], name, mro, attrs) -> Any: ...

def data_provider(*data_sets) -> Callable[[Any], Any]: ...
