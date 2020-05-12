# (generated with --quick)

import components.vera
import datetime
from typing import Any, Type

ENTITY_ID_FORMAT: Any
Entity: Any
SCAN_INTERVAL: datetime.timedelta
TEMP_CELSIUS: Any
TEMP_FAHRENHEIT: Any
VERA_CONTROLLER: str
VERA_DEVICES: str
VeraDevice: Type[components.vera.VeraDevice]
_LOGGER: logging.Logger
convert: Any
logging: module
timedelta: Type[datetime.timedelta]

class VeraSensor(components.vera.VeraDevice, Any):
    __doc__: str
    _temperature_units: Any
    current_value: Any
    entity_id: Any
    last_changed_time: Any
    state: Any
    unit_of_measurement: Any
    def update(self) -> None: ...

def setup_platform(hass, config, add_entities, discovery_info = ...) -> None: ...
