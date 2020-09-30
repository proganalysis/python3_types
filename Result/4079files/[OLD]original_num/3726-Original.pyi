# (generated with --quick)

import elements.icons
import elements.label
from typing import Any, Type

eventLabel: Type[elements.label.eventLabel]
eventWorker: Any
gui: Any
hasconst: Any
icons: elements.icons.mdiIcons
log: logging.Logger
logging: module
media_player: module
moosegesture: Any
pygame: Any

class Header(Any):
    pcls: str
    state: int
    def __init__(self, name, **kwargs) -> None: ...
    def event(self, e) -> None: ...

class Light(Any):
    haevent: Any
    pcls: str
    state: int
    def __init__(self, haevent, **kwargs) -> None: ...
    def callback(self) -> None: ...
    def event(self, e) -> None: ...
    def set_hass_event(self, haevent) -> None: ...

class LightSwitch(Any):
    _value: bool
    haevent: Any
    def __init__(self, haevent, **kwargs) -> None: ...
    def callback(self) -> None: ...
    def click(self) -> None: ...
    def set_hass_event(self, haevent) -> None: ...

class Scrollable(Any):
    hscroll: int
    inMotion: Any
    prevLocs: list
    scroll_horizontal: Any
    vscroll: int
    def __init__(self, widget, width, height, scroll_horizontal = ..., **params) -> None: ...
    def addPrevLoc(self, loc) -> None: ...
    def motion(self, _event) -> None: ...
    def setMotion(self, motion) -> None: ...

class Sensor(Any):
    haevent: Any
    pcls: str
    state: int
    def __init__(self, haevent, **kwargs) -> None: ...
    def event(self, e) -> None: ...
    def set_hass_event(self, haevent) -> None: ...

class rowHeader(rowLight):
    btn_cls: str
    entity: Any
    icon: None
    ligth_width: Any
    sw_cls: str
    widget: Any
    width: Any
    def __init__(self, entity, width = ..., table = ...) -> None: ...

class rowLight(object):
    btn_cls: str
    entity: Any
    icon: str
    iconButton: Any
    light: Light
    ligth_width: Any
    sw_cls: str
    switch: Any
    widget: Any
    width: Any
    def __init__(self, entity, last = ..., width = ..., table = ...) -> None: ...
    def draw(self) -> Any: ...
    def set_hass_event(self, event) -> None: ...

class rowSensor(object):
    btn_cls: str
    entity: Any
    icon: Any
    iconButton: Any
    sensorName: Sensor
    sensorName_width: Any
    state: sensorValue
    sw_cls: str
    widget: Any
    width: Any
    def __init__(self, entity, last = ..., width = ...) -> None: ...
    def draw(self) -> Any: ...
    def set_hass_event(self, event) -> None: ...

class sensorValue(Any):
    haevent: Any
    sValue: Any
    value: Any
    def __init__(self, haevent, **kwargs) -> None: ...
    def event(self, e) -> None: ...
    def set_hass_event(self, haevent) -> None: ...

def __getattr__(name) -> Any: ...
