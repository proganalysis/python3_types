# (generated with --quick)

import datetime
from typing import Any, Dict, List, Optional, Type

ATTR_ATTRIBUTION: Any
CONF_API_KEY: Any
CONF_ATTRIBUTION: str
CONF_FORECAST: str
CONF_LANGUAGE: str
CONF_MONITORED_CONDITIONS: Any
CONF_NAME: Any
DEFAULT_NAME: str
Entity: Any
MIN_TIME_BETWEEN_UPDATES: datetime.timedelta
PLATFORM_SCHEMA: Any
REQUIREMENTS: List[str]
SENSOR_TYPES: Dict[str, list]
TEMP_CELSIUS: Any
TEMP_FAHRENHEIT: Any
Throttle: Any
_LOGGER: logging.Logger
cv: Any
logging: module
timedelta: Type[datetime.timedelta]
vol: Any

class OpenWeatherMapSensor(Any):
    __doc__: str
    _name: Any
    _state: Any
    _unit_of_measurement: Any
    client_name: Any
    device_state_attributes: Dict[Any, str]
    name: str
    owa_client: Any
    state: Any
    temp_unit: Any
    type: Any
    unit_of_measurement: Any
    def __init__(self, name, weather_data, sensor_type, temp_unit) -> None: ...
    def update(self) -> None: ...

class WeatherData(object):
    __doc__: str
    data: None
    fc_data: None
    forecast: Any
    latitude: Any
    longitude: Any
    owm: Any
    update: Any
    def __init__(self, owm, forecast, latitude, longitude) -> None: ...

def setup_platform(hass, config, add_devices, discovery_info = ...) -> Optional[bool]: ...
