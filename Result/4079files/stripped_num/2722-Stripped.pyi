# (generated with --quick)

from typing import Any, Generator

RandProb: Any

class Master(Any):
    __slots__ = ["A", "B", "ack", "clk", "data", "rdy", "strict"]
    A: Any
    B: Any
    ack: Any
    clk: Any
    data: Any
    rdy: Any
    strict: Any
    values: Any
    def Send(self, data, imm = ...) -> Generator[Any, Any, None]: ...
    def SendIter(self, it) -> Generator[Any, Any, None]: ...
    def _D(self, data) -> None: ...
    def _X(self) -> None: ...
    def __init__(self, rdy, ack, data, clk, A = ..., B = ..., callbacks = ..., strict = ...) -> None: ...

class Slave(Any):
    __slots__ = ["A", "B", "ack", "clk", "data", "rdy"]
    A: Any
    B: Any
    ack: Any
    clk: Any
    data: Any
    rdy: Any
    def Monitor(self) -> generator: ...
    def __init__(self, rdy, ack, data, clk, A = ..., B = ..., callbacks = ...) -> None: ...

def __getattr__(name) -> Any: ...
