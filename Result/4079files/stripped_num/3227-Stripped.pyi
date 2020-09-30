# (generated with --quick)

from typing import Any, List

BitVector: Any
CLK: Any
CoreIRSimulator: Any
I: Any
N: int
O: Any
enable: Any
j: int
m: Any
mantle: Any
outputs: List[list]
simulator: Any
waveform: Any

class ShiftRegisterNCE(Any):
    IO: list
    name: str
    @classmethod
    def definition(siso) -> Any: ...

def DefineShiftRegister(n, init = ..., has_ce = ..., has_reset = ...) -> type: ...
