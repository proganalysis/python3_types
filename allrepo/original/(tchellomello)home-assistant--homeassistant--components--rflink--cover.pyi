# (generated with --quick)

from typing import Any, Coroutine, List

CONF_ALIASES: Any
CONF_DEVICES: Any
CONF_DEVICE_DEFAULTS: Any
CONF_FIRE_EVENT: Any
CONF_GROUP: Any
CONF_GROUP_ALIASES: Any
CONF_NAME: Any
CONF_NOGROUP_ALIASES: Any
CONF_SIGNAL_REPETITIONS: Any
CoverDevice: Any
DEVICE_DEFAULTS_SCHEMA: Any
PLATFORM_SCHEMA: Any
RestoreEntity: Any
RflinkCommand: Any
STATE_OPEN: Any
_LOGGER: logging.Logger
cv: Any
logging: module
vol: Any

class RflinkCover(Any, Any, Any):
    __doc__: str
    _state: Any
    assumed_state: bool
    is_closed: bool
    should_poll: bool
    def _handle_event(self, event) -> None: ...
    def async_added_to_hass(self) -> Coroutine[Any, Any, None]: ...
    def async_close_cover(self, **kwargs) -> Any: ...
    def async_open_cover(self, **kwargs) -> Any: ...
    def async_stop_cover(self, **kwargs) -> Any: ...

def async_setup_platform(hass, config, async_add_entities, discovery_info = ...) -> Coroutine[Any, Any, None]: ...
def devices_from_config(domain_config) -> List[RflinkCover]: ...
