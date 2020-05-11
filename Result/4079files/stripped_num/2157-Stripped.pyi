# (generated with --quick)

from typing import Any

ECDSA: Any
Fixed8: Any
Transaction: Any
TransactionType: Any
settings: Any
sys: module

class EnrollmentTransaction(Any):
    PublicKey: Any
    Type: Any
    _script_hash: None
    def DeserializeExclusiveData(self, reader) -> None: ...
    def SerializeExclusiveData(self, writer) -> None: ...
    def Size(self) -> Any: ...
    def SystemFee(self) -> Any: ...
    def ToJson(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
