# (generated with --quick)

import __builtin__
from typing import Any, List

__all__: List[str]
base32: Any
datetime: module
hints: Any
uuid: module

class MemoryView:
    __slots__ = ["memory"]
    __doc__: __builtin__.str
    bytes: Any
    int: __builtin__.int
    memory: memoryview
    str: Any
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> __builtin__.int: ...
    def __init__(self, buffer) -> None: ...
    def __int__(self) -> __builtin__.int: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __repr__(self) -> __builtin__.str: ...
    def __str__(self) -> Any: ...

class Randomness(MemoryView):
    __slots__ = ["memory"]
    __doc__: __builtin__.str
    memory: memoryview
    str: Any

class Timestamp(MemoryView):
    __slots__ = ["memory"]
    __doc__: __builtin__.str
    datetime: datetime.datetime
    memory: memoryview
    str: Any
    timestamp: Any

class ULID(MemoryView):
    __slots__ = ["memory"]
    __doc__: __builtin__.str
    memory: memoryview
    str: Any
    uuid: uuid.UUID
    def randomness(self) -> Randomness: ...
    def timestamp(self) -> Timestamp: ...
