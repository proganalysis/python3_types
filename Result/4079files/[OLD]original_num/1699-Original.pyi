# (generated with --quick)

from typing import Any, Dict, List, Optional

Plugin: Any
TestPluginCommon: Any
stablehash: Any

class Highway_Parking_Lane(Any):
    parking_condition: str
    parking_lane: str
    def init(self, logger) -> None: ...
    def way(self, data, tags, nds) -> Optional[List[Dict[str, Any]]]: ...

class Test(Any):
    def test(self) -> None: ...
