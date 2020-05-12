# (generated with --quick)

import datetime
from typing import Any, List, Type

ATTR_BATTERY_LEVEL: Any
ATTR_BIKE_FRAME_NUMBER: str
ATTR_BIKE_SERIAL_NUMBER: str
ATTR_EMAIL: str
ATTR_FIRMWARE_VERSION: str
ATTR_FRIENDLY_NAME: Any
ATTR_FULL_NAME: str
ATTR_IMEI: str
ATTR_LAST_SEEN: str
ATTR_NAME: Any
ATTR_STATE: str
ATTR_USER_ID: str
CONF_PASSWORD: Any
CONF_USERNAME: Any
ConfigType: Any
ENTITY_ID_FORMAT: Any
EVENT_SHERLOCK_ALARM: str
MIN_TIME_BETWEEN_SCANS: datetime.timedelta
PLATFORM_SCHEMA: Any
REQUIREMENTS: List[str]
SOURCE_TYPE_GPS: Any
STATE_ALARM: str
_LOGGER: logging.Logger
cv: Any
dt_util: Any
logging: module
slugify: Any
timedelta: Type[datetime.timedelta]
track_time_interval: Any
vol: Any

class SherlockBikeScanner:
    __doc__: str
    hass: Any
    password: Any
    see: Any
    service: Any
    success_init: bool
    username: Any
    def __init__(self, hass, config, see) -> None: ...
    def _update_info(self, now = ...) -> None: ...

def setup_scanner(hass, config, see, discovery_info = ...) -> bool: ...
