# (generated with --quick)

from typing import Any, Dict, Union

AllOps: Any
HlsAllocator: Any
HlsScheduler: Any

class DebugHlsPlatform:
    OP_LATENCIES: Dict[Any, Union[float, int]]
    __doc__: str
    allocator: Any
    scheduler: Any
    def __init__(self) -> None: ...
    def onHlsInit(self, hls) -> None: ...
