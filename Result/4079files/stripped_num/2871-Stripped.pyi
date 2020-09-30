# (generated with --quick)

from typing import Any, Coroutine, Optional

CONF_NAME: Any
CONF_UNIT_OF_MEASUREMENT: Any
DEFAULT_NAME: str
Entity: Any
ICON: str
PLATFORM_SCHEMA: Any
_LOGGER: logging.Logger
cv: Any
dt_util: Any
logging: module
vol: Any

class UptimeSensor(Any):
    __doc__: str
    _name: Any
    _state: Optional[float]
    _unit: Any
    icon: str
    initial: Any
    name: Any
    state: Any
    unit_of_measurement: Any
    def __init__(self, name, unit) -> None: ...
    def async_update(self) -> Coroutine[Any, Any, None]: ...

def async_setup_platform(hass, config, async_add_entities, discovery_info = ...) -> Coroutine[Any, Any, None]: ...
