# (generated with --quick)

from typing import Any, Callable, Optional, Type, TypeVar

Min: MinType

_T = TypeVar('_T')

class MinType(object):
    __doc__: str

class Sort:
    key: Any
    key_condition: Callable[[Any], Any]
    key_condition_dict: Callable[[Any], Any]
    reverse: Any
    def __init__(self, key, reverse = ...) -> None: ...
    def __str__(self) -> str: ...
    def sort(self, variants_collection, inplace = ...) -> list: ...
    def sort_dict(self, variants_exposed, inplace = ...) -> Optional[list]: ...

def sort_from_request(request) -> Sort: ...
def total_ordering(cls: Type[_T]) -> Type[_T]: ...
