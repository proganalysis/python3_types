# (generated with --quick)

import enum
from typing import Any, Callable, Type

Enum: Type[enum.Enum]
collections: module

class RangedCodeEnum(enum.Enum):
    @classmethod
    def from_code(cls, value) -> Any: ...

def opencls(cls) -> Callable[[Any], Any]: ...
