# (generated with --quick)

from typing import Any, List

BASE_TYPES: List[str]
COMPOSITE_PATTERN: str
COMPOSITE_TYPES: List[str]
DatatypeError: Any
re: module

class Type:
    __doc__: str
    children: Any
    first_child: Any
    is_composite: bool
    name: Any
    def __init__(self, name, children = ...) -> None: ...
    def __str__(self) -> Any: ...
    @classmethod
    def from_string(cls, string) -> Type: ...
