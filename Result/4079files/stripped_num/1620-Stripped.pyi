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
    status: Any
    valid_statuses: Set[bytes]
    value: Any
    def __bytes__(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, status) -> None: ...
    @classmethod
    def parse(cls, buf, params) -> Tuple[Any, Any]: ...
