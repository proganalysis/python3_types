# (generated with --quick)

from typing import Any

ATTR_TEMPERATURE: Any
BuderusBridge: Any
ClimateDevice: Any
DOMAIN: Any
SUPPORT_FLAGS: Any
SUPPORT_TARGET_TEMPERATURE: Any
TEMP_CELSIUS: Any
logging: module

class BuderusThermostat(Any):
    __doc__: str
    _bridge: Any
    _current_temperature: Any
    _name: Any
    _target_temperature: Any
    current_temperature: Any
    logger: logging.Logger
    name: Any
    supported_features: Any
    target_temperature: Any
    temperature_unit: Any
    def __init__(self, name, bridge) -> None: ...
    def set_temperature(self, **kwargs) -> None: ...
    def update(self) -> None: ...

def setup_platform(hass, config, add_devices, discovery_info = ...) -> None: ...
