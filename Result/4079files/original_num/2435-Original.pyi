# (generated with --quick)

from typing import Any

AutoField: Any
BigIntegerField: Any
BooleanField: Any
CharField: Any
DateField: Any
DecimalField: Any
EmailField: Any
Field: Any
ForeignKey: Any
IntegerField: Any
TextField: Any
UUIDField: Any
logging: module

class PatchedField(Any):
    __doc__: str
    _db_comment: Any
    db_comment: Any
    def __init__(self, *args, **kwargs) -> None: ...

def patch_fields() -> None: ...
