# (generated with --quick)

from typing import Any, Dict, List

DOMAIN: Any
HUB_ADDRESS: str
REQUIREMENTS: List[str]
Scene: Any
_LOGGER: logging.Logger
generate_entity_id: Any
logging: module

class PowerViewScene(Any):
    __doc__: str
    device_state_attributes: Dict[str, Any]
    entity_id: Any
    entity_id_format: Any
    hass: Any
    icon: str
    name: str
    pv_instance: Any
    scene_data: Any
    def __init__(self, hass, scene_data, room_data, pv_instance) -> None: ...
    def _sync_room_data(self, room_data) -> None: ...
    def activate(self) -> None: ...

def setup_platform(hass, config, add_devices, discovery_info = ...) -> bool: ...
