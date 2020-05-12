# (generated with --quick)

from typing import Any

MatchQuality: Any
SendErrorCheckingRPCRecord: Any

class PersistGraphRecord(Any):
    RPC_ID: int
    __doc__: str
    @classmethod
    def FromBinary(cls, record_data, record_count = ...) -> PersistGraphRecord: ...
    @classmethod
    def MatchQuality(cls, record_data, record_count = ...) -> Any: ...
    def __init__(self, address) -> None: ...
    def __str__(self) -> str: ...
