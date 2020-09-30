# (generated with --quick)

from typing import Any, Optional, Type

ATTR_CREATED_AT: Any
ATTR_ID: Any
ATTR_NAME: Any
Command: Any
datetime: Type[datetime.datetime]

class ApiResource:
    __doc__: str
    created_at: Optional[datetime.datetime]
    id: Any
    name: Any
    raw: Any
    def __init__(self, raw) -> None: ...
    def observe(self, callback, err_callback, duration = ...) -> Any: ...
    def set_name(self, name) -> Any: ...
    def set_values(self, values) -> Any: ...
    def update(self) -> Any: ...
