from pygame.locals import *
from pgu.gui.const import *
from . import remote as remote
from pgu import gui
from typing import Any, Optional

log: Any
whereami: Any

class mdiIcons:
    icons: Any = ...
    def __init__(self, css_file: Any, ttf_file: Any) -> None: ...
    def icon(self, iconName: Any, size: int = ..., color: str = ..., scale: str = ...): ...

icons: Any

class Scrollable(gui.SlideBox):
    inMotion: bool = ...
    prevLocs: Any = ...
    hscroll: int = ...
    vscroll: int = ...
    scroll_horizontal: Any = ...
    def __init__(self, widget: Any, width: Any, height: Any, scroll_horizontal: bool = ..., **params: Any) -> None: ...
    offset: Any = ...
    def setMotion(self, motion: Any) -> None: ...
    def addPrevLoc(self, loc: Any) -> None: ...
    def motion(self, _event: Any) -> None: ...

class Light(gui.Button):
    haevent: Any = ...
    def __init__(self, haevent: Any, **kwargs: Any) -> None: ...
    def callback(self) -> None: ...
    state: int = ...
    pcls: str = ...
    def set_hass_event(self, haevent: Any) -> None: ...
    def event(self, e: Any) -> None: ...

class Sensor(gui.Button):
    haevent: Any = ...
    def __init__(self, haevent: Any, **kwargs: Any) -> None: ...
    state: int = ...
    pcls: str = ...
    def set_hass_event(self, haevent: Any) -> None: ...
    def event(self, e: Any) -> None: ...

class LightSwitch(gui.Switch):
    haevent: Any = ...
    def __init__(self, haevent: Any, **kwargs: Any) -> None: ...
    def callback(self) -> None: ...
    def click(self) -> None: ...
    _value: bool = ...
    def set_hass_event(self, haevent: Any) -> None: ...

class Header(gui.Button):
    pcls: str = ...
    state: int = ...
    def __init__(self, name: Any, **kwargs: Any) -> None: ...
    def event(self, e: Any) -> None: ...

class sensorValue(gui.Button):
    haevent: Any = ...
    def __init__(self, haevent: Any, **kwargs: Any) -> None: ...
    sValue: Any = ...
    value: Any = ...
    def set_hass_event(self, haevent: Any) -> None: ...
    def event(self, e: Any) -> None: ...

class eventLabel(gui.Label):
    haevent: Any = ...
    def __init__(self, entity: Any) -> None: ...
    value: Any = ...
    def set_hass_event(self, haevent: Any) -> None: ...

class rowLight:
    width: Any = ...
    widget: Any = ...
    entity: Any = ...
    btn_cls: str = ...
    sw_cls: str = ...
    ligth_width: Any = ...
    icon: str = ...
    def __init__(self, entity: Any, last: bool = ..., width: int = ..., table: Optional[Any] = ...) -> None: ...
    def set_hass_event(self, event: Any) -> None: ...
    iconButton: Any = ...
    light: Any = ...
    switch: Any = ...
    def draw(self): ...

class rowSensor:
    width: Any = ...
    widget: Any = ...
    entity: Any = ...
    btn_cls: str = ...
    sw_cls: str = ...
    sensorName_width: Any = ...
    icon: Any = ...
    def __init__(self, entity: Any, last: bool = ..., width: int = ...) -> None: ...
    def set_hass_event(self, event: Any) -> None: ...
    iconButton: Any = ...
    state: Any = ...
    sensorName: Any = ...
    def draw(self): ...

class rowHeader(rowLight):
    width: Any = ...
    icon: Any = ...
    btn_cls: str = ...
    def __init__(self, entity: Any, width: int = ..., table: Optional[Any] = ...) -> None: ...
