# (generated with --quick)

from typing import Any

AllOps: Any
Hls: Any
HlsConst: Any
HlsOperation: Any
HlsRead: Any
HlsWrite: Any
If: Any
RtlSignal: Any
end_clk: Any
epsilon: Any
getSignalName: Any
start_clk: Any

class HlsAllocator:
    __doc__: str
    _reg: Any
    _sig: Any
    node2instance: dict
    parentHls: Any
    def __init__(self, parentHls) -> None: ...
    def _instantiate(self, node) -> Any: ...
    def allocate(self) -> None: ...
    def inistanciateWrite(self, write) -> Any: ...
    def instanciateRead(self, readOp) -> TimeIndependentRtlResource: ...
    def instantiateOperation(self, node) -> TimeIndependentRtlResource: ...

class TimeIndependentRtlResource:
    INVARIANT_TIME: str
    __doc__: str
    allocator: Any
    timeOffset: Any
    valuesInTime: list
    def __init__(self, signal, time, hlsAllocator) -> None: ...
    def get(self, time) -> Any: ...
