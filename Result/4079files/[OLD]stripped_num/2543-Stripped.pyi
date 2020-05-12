# (generated with --quick)

from typing import Any, Generator, Tuple

np: module

class Master(Any):
    __slots__ = ["HRANGE", "HSYNC", "HVALID", "VRANGE", "VSYNC", "VVALID", "clk", "data", "hsync", "strict", "vsync"]
    HRANGE: Any
    HSYNC: Any
    HVALID: Any
    VRANGE: Any
    VSYNC: Any
    VVALID: Any
    clk: Any
    data: Any
    hsync: Any
    strict: Any
    values: Any
    vsync: Any
    def SendFrame(self, frame) -> Generator[nothing, Any, None]: ...
    def SendFrames(self, frames) -> Generator[nothing, Any, None]: ...
    def _FrameBody(self, frame) -> Generator[Any, Any, None]: ...
    def _FrameEnd(self) -> Generator[Any, Any, None]: ...
    def _Translate(self, timing) -> Tuple[Any, Any, Any]: ...
    def __init__(self, vsync, hsync, data, clk, VTIMING, HTIMING, callbacks = ..., strict = ...) -> None: ...

def __getattr__(name) -> Any: ...
