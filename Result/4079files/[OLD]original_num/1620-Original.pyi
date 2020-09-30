# (generated with --quick)

from typing import Any, List, Set, Tuple

Atom: Any
InvalidContent: Any
NotParseable: Any
Params: Any
Parseable: Any
Space: Any
__all__: List[str]

class StatusAttribute(Any):
    __doc__: str
    status: bytes
    valid_statuses: Set[bytes]
    value: bytes
    def __bytes__(self) -> bytes: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, status: bytes) -> None: ...
    @classmethod
    def parse(cls, buf: memoryview, params) -> Tuple[StatusAttribute, memoryview]: ...
