# (generated with --quick)

from typing import Any, Dict

BuderusBridge: Any
CONF_RESOURCES: Any
DOMAIN: Any
Entity: Any
SENSOR_TYPES: Dict[str, list]
TEMP_CELSIUS: Any
_LOGGER: logging.Logger
logging: module

class BuderusSensor(Any):
    __doc__: str
    _bridge: Any
    _icon: Any
    _km_id: Any
    _name: Any
    _sensor_type: Any
    _state: Any
    _unit: Any
    icon: Any
    name: Any
    state: Any
    unit_of_measurement: Any
    def __init__(self, name, bridge, sensor_type, unit, icon, km_id) -> None: ...
    def update(self) -> None: ...

def setup_platform(hass, config, add_devices, discovery_info = ...) -> None: ...
