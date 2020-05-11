# (generated with --quick)

import collections
from typing import Any, Callable, Coroutine, Dict, Iterable, List, Optional, Sequence, Sized, Tuple, Type, TypeVar, Union

Map = `namedtuple-map-attribute-name-default_unit-device_class`

Attribute: Any
CAPABILITY_TO_SENSORS: Dict[Any, List[`namedtuple-map-attribute-name-default_unit-device_class`]]
Capability: Any
DATA_BROKERS: Any
DEVICE_CLASS_BATTERY: Any
DEVICE_CLASS_HUMIDITY: Any
DEVICE_CLASS_ILLUMINANCE: Any
DEVICE_CLASS_TEMPERATURE: Any
DEVICE_CLASS_TIMESTAMP: Any
DOMAIN: Any
ENERGY_KILO_WATT_HOUR: Any
MASS_KILOGRAMS: Any
POWER_WATT: Any
SmartThingsEntity: Any
TEMP_CELSIUS: Any
TEMP_FAHRENHEIT: Any
THREE_AXIS_NAMES: List[str]
UNITS: Dict[str, Any]

_Tnamedtuple-map-attribute-name-default_unit-device_class = TypeVar('_Tnamedtuple-map-attribute-name-default_unit-device_class', bound=`namedtuple-map-attribute-name-default_unit-device_class`)

class SmartThingsSensor(Any):
    __doc__: str
    _attribute: str
    _default_unit: str
    _device_class: str
    _name: str
    device_class: Any
    name: str
    state: Any
    unique_id: str
    unit_of_measurement: Any
    def __init__(self, device, attribute: str, name: str, default_unit: str, device_class: str) -> None: ...

class SmartThingsThreeAxisSensor(Any):
    __doc__: str
    _index: Any
    name: str
    state: Any
    unique_id: str
    def __init__(self, device, index) -> None: ...

class `namedtuple-map-attribute-name-default_unit-device_class`(tuple):
    __slots__ = ["attribute", "default_unit", "device_class", "name"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str]
    attribute: Any
    default_unit: Any
    device_class: Any
    name: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-map-attribute-name-default_unit-device_class`], attribute, name, default_unit, device_class) -> `_Tnamedtuple-map-attribute-name-default_unit-device_class`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-map-attribute-name-default_unit-device_class`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-map-attribute-name-default_unit-device_class`: ...
    def _replace(self: `_Tnamedtuple-map-attribute-name-default_unit-device_class`, **kwds) -> `_Tnamedtuple-map-attribute-name-default_unit-device_class`: ...

def async_setup_entry(hass, config_entry, async_add_entities) -> Coroutine[Any, Any, None]: ...
def async_setup_platform(hass, config, async_add_entities, discovery_info = ...) -> Coroutine[Any, Any, None]: ...
def get_capabilities(capabilities: Sequence[str]) -> Optional[Sequence[str]]: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
