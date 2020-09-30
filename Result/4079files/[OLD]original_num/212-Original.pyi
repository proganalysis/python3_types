# (generated with --quick)

from typing import Any, List, Optional

BASE_TYPES: List[str]
COMPOSITE_PATTERN: str
COMPOSITE_TYPES: List[str]
DatatypeError: Any
re: module

class Type:
    __doc__: str
    children: Any
    first_child: Type
    is_composite: bool
    name: str
    def __init__(self, name: str, children: Optional[List[Type]] = ...) -> None: ...
    def __str__(self) -> str: ...
    @classmethod
    def from_string(cls, string: str) -> Type: ...
