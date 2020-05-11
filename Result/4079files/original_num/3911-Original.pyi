# (generated with --quick)

from typing import Any

Base: Any
Column: Any
DateTime: Any
Integer: Any
String: Any
UUID: Any
func: Any
uuid: module

class Parameter(Any):
    __tablename__: str
    created_timestamp: Any
    group_id: Any
    id: Any
    name: Any
    value: Any
    def __init__(self, group_id: uuid.UUID, name: str, value: str) -> None: ...
