from typing import Any, List, Optional

BASE_TYPES: Any
COMPOSITE_TYPES: Any
COMPOSITE_PATTERN: str

class Type:
    name: str
    children: Optional[List[Type]]
    @classmethod
    def from_string(cls: Any, string: str) -> Type: ...
    def __init__(self, name: str, children: Optional[List[Type]]=...) -> None: ...
    @property
    def is_composite(self) -> bool: ...
    @property
    def first_child(self) -> Type: ...
    def __str__(self) -> str: ...
