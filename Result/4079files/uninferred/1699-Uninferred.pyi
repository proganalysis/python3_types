from plugins.Plugin import Plugin, TestPluginCommon
from typing import Any

class Highway_Parking_Lane(Plugin):
    parking_lane: str = ...
    parking_condition: str = ...
    def init(self, logger: Any) -> None: ...
    def way(self, data: Any, tags: Any, nds: Any): ...

class Test(TestPluginCommon):
    def test(self) -> None: ...
