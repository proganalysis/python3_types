# (generated with --quick)

from typing import Any, Callable, Coroutine, Dict

CONF_ALARM: str
CONF_CODE: Any
CONF_DELAYED: str
CONF_DISARM_AFTER_TRIGGER: Any
CONF_HEADSUP: str
CONF_IMMEDIATE: str
CONF_NAME: Any
CONF_NOTATHOME: str
CONF_PENDING_TIME: Any
CONF_PLATFORM: Any
CONF_TRIGGER_TIME: Any
CONF_WARNING: str
EVENT_STATE_CHANGED: Any
EVENT_TIME_CHANGED: Any
PLATFORM_SCHEMA: Any
STATE_ALARM_ARMED_AWAY: Any
STATE_ALARM_ARMED_HOME: Any
STATE_ALARM_DISARMED: Any
STATE_ALARM_PENDING: Any
STATE_ALARM_TRIGGERED: Any
STATE_ALARM_WARNING: str
STATE_ON: Any
_LOGGER: logging.Logger
alarm: Any
async_track_point_in_time: Any
asyncio: module
cv: Any
datetime: module
enum: module
logging: module
now: Any
re: module
switch: Any
vol: Any

class BWAlarm(Any):
    _alarm: Any
    _allinputs: set
    _allsensors: set
    _delayed: set
    _hass: Any
    _immediate: set
    _lasttrigger: Any
    _name: Any
    _notathome: set
    _pending_time: datetime.timedelta
    _returnto: Any
    _state: Any
    _timeoutat: Any
    _trigger_time: datetime.timedelta
    _warning: Any
    changed_by: Any
    delayed: set
    device_state_attributes: Dict[str, Any]
    ignored: set
    immediate: set
    name: Any
    should_poll: bool
    state: Any
    def __init__(self, hass, config) -> None: ...
    def alarm_arm_away(self, code = ...) -> None: ...
    def alarm_arm_home(self, code = ...) -> None: ...
    def alarm_disarm(self, code = ...) -> None: ...
    def alarm_trigger(self, code = ...) -> None: ...
    def clearsignals(self) -> None: ...
    def noton(self, eid) -> bool: ...
    def process_event(self, event) -> None: ...
    def setsignals(self, athome) -> None: ...
    def state_change_listener(self, event) -> None: ...
    def time_change_listener(self, eventignored) -> None: ...

class Events(enum.Enum):
    ArmAway: int
    ArmHome: int
    DelayedTrip: int
    Disarm: int
    ImmediateTrip: int
    Timeout: int
    Trigger: int

def async_setup_platform(hass, config, async_add_devices, discovery_info = ...) -> Coroutine[Any, Any, None]: ...
def attrgetter(*attrs: str) -> Callable[[Any], tuple]: ...
