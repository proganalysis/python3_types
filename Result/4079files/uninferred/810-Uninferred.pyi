from enum import Enum
from typing import Any

class RangedCodeEnum(Enum):
    @classmethod
    def from_code(cls, value: Any): ...

def opencls(cls): ...
