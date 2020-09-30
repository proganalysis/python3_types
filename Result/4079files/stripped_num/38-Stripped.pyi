# (generated with --quick)

from typing import Any, Dict, List

ALARM: str
AUTHOR: Any
BATTERY: str
CAPABILITIES: Dict[Any, bool]
COMMANDS: List[nothing]
DEVICE_TYPE_MOTION: Any
REQUESTS: list
WATER: Any
WaterSensor: Any
ZWaveNode: Any
ZWaveValue: Any
ZwaveDevice: Any
logging: Any

class ZwaveWaterSensor(Any, Any):
    _node: Any
    refreshed: bool
    value_map: Any
    def __init__(self, firefly, package, title = ..., initial_values = ..., value_map = ..., **kwargs) -> None: ...
    def export(self, current_values = ..., api_view = ..., **kwargs) -> Any: ...
    def update_from_zwave(self, node = ..., ignore_update = ..., values = ..., values_only = ..., **kwargs) -> None: ...
