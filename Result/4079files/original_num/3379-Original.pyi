# (generated with --quick)

from typing import Any, Dict

AllOps: Any
HwtSerializerCtx: Any

class HwtSerializer_ops:
    _binOps: Dict[Any, str]
    _castOps: set
    _unaryOps: Dict[Any, str]
    opPrecedence: Dict[Any, int]
    @classmethod
    def Operator(cls, op, ctx) -> Any: ...
