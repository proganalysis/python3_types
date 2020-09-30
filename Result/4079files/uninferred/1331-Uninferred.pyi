import magma as m
from typing import Any

def clb(a: Any, b: Any, c: Any, d: Any): ...

T: Any

class Combinational(m.Circuit):
    name: str = ...
    IO: Any = ...
    @classmethod
    def definition(io: Any) -> None: ...

simulator: Any
a: Any
b: Any
