# (generated with --quick)

import components.homekit_controller
from typing import Any, Coroutine, Type

BRIGHTNESS_ICON: str
HUMIDITY_ICON: str
HomeKitEntity: Type[components.homekit_controller.HomeKitEntity]
KNOWN_DEVICES: Any
TEMP_CELSIUS: Any
TEMP_C_ICON: str
UNIT_LUX: str
UNIT_PERCENT: str

class HomeKitHumiditySensor(components.homekit_controller.HomeKitEntity):
    __doc__: str
    _state: Any
    icon: str
    name: str
    state: Any
    unit_of_measurement: str
    def __init__(self, *args) -> None: ...
    def _update_relative_humidity_current(self, value) -> None: ...
    def get_characteristic_types(self) -> list: ...

class HomeKitLightSensor(components.homekit_controller.HomeKitEntity):
    __doc__: str
    _state: Any
    icon: str
    name: str
    state: Any
    unit_of_measurement: str
    def __init__(self, *args) -> None: ...
    def _update_light_level_current(self, value) -> None: ...
    def get_characteristic_types(self) -> list: ...

class HomeKitTemperatureSensor(components.homekit_controller.HomeKitEntity):
    __doc__: str
    _state: Any
    icon: str
    name: str
    state: Any
    unit_of_measurement: Any
    def __init__(self, *args) -> None: ...
    def _update_temperature_current(self, value) -> None: ...
    def get_characteristic_types(self) -> list: ...

def async_setup_entry(hass, config_entry, async_add_entities) -> Coroutine[Any, Any, None]: ...
def async_setup_platform(hass, config, async_add_entities, discovery_info = ...) -> Coroutine[Any, Any, None]: ...
