from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import slugify as slugify
from typing import Any, Optional

REQUIREMENTS: Any
_LOGGER: Any
ATTR_EMAIL: str
ATTR_FIRMWARE_VERSION: str
ATTR_FULL_NAME: str
ATTR_IMEI: str
ATTR_LAST_SEEN: str
ATTR_BIKE_FRAME_NUMBER: str
ATTR_BIKE_SERIAL_NUMBER: str
ATTR_STATE: str
ATTR_USER_ID: str
EVENT_SHERLOCK_ALARM: str
MIN_TIME_BETWEEN_SCANS: Any
STATE_ALARM: str

def setup_scanner(hass: Any, config: ConfigType, see: Any, discovery_info: Any=...) -> Any: ...

class SherlockBikeScanner:
    hass: Any = ...
    see: Any = ...
    username: Any = ...
    password: Any = ...
    service: Any = ...
    success_init: bool = ...
    def __init__(self, hass: Any, config: ConfigType, see: Any) -> None: ...
    def _update_info(self, now: Optional[Any] = ...) -> None: ...
