# (generated with --quick)

from typing import Any, List

CONF_NAME: Any
CONF_PAYLOAD: Any
CONF_UNIT_OF_MEASUREMENT: Any
CONF_VARIABLE: str
DEFAULT_NAME: str
DEPENDENCIES: List[str]
Entity: Any
PLATFORM_SCHEMA: Any
STATE_UNKNOWN: Any
_LOGGER: logging.Logger
cv: Any
logging: module
pilight: Any
vol: Any

class PilightSensor(Any):
    __doc__: str
    _hass: Any
    _name: Any
    _payload: Any
    _state: Any
    _unit_of_measurement: Any
    _variable: Any
    name: Any
    should_poll: bool
    state: Any
    unit_of_measurement: Any
    def __init__(self, hass, name, variable, payload, unit_of_measurement) -> None: ...
    def _handle_code(self, call) -> None: ...

def setup_platform(hass, config, add_devices, discovery_info = ...) -> None: ...
