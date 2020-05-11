# (generated with --quick)

from typing import Any, Dict, List, Type
import vmrayclient

Analyzer: Any
VMRayClient: Type[vmrayclient.VMRayClient]

class VMRayAnalyzer(Any):
    __doc__: str
    url: Any
    vmrc: vmrayclient.VMRayClient
    def __init__(self) -> None: ...
    def run(self) -> None: ...
    def summary(self, raw) -> Dict[str, List[Dict[str, Any]]]: ...
