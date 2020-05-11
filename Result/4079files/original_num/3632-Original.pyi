# (generated with --quick)

from typing import Any, Callable, Coroutine, List, Optional

base64: module
iterm2: Any
json: module
typing: module

class CheckboxKnob:
    _CheckboxKnob__knob: Knob
    __doc__: str
    def __init__(self, name: str, default_value: bool, key: str) -> None: ...
    def to_proto(self) -> Any: ...

class ColorKnob:
    _ColorKnob__knob: Knob
    __doc__: str
    def __init__(self, name: str, default_value, key: str) -> None: ...
    def to_proto(self) -> Any: ...

class Knob:
    _Knob__json_default_value: Any
    _Knob__key: Any
    _Knob__name: Any
    _Knob__placeholder: Any
    _Knob__type: Any
    def __init__(self, type, name, placeholder, json_default_value, key) -> None: ...
    def to_proto(self) -> Any: ...

class PositiveFloatingPointKnob:
    _PositiveFloatingPointKnob__knob: Knob
    __doc__: str
    def __init__(self, name: str, default_value: float, key: str) -> None: ...
    def to_proto(self) -> Any: ...

class StatusBarComponent:
    Icon: type
    _StatusBarComponent__connection: Any
    _StatusBarComponent__detailed_description: str
    _StatusBarComponent__exemplar: str
    _StatusBarComponent__icons: list
    _StatusBarComponent__identifier: str
    _StatusBarComponent__knobs: List[Knob]
    _StatusBarComponent__short_description: str
    _StatusBarComponent__update_cadence: Optional[float]
    __doc__: str
    def __init__(self, short_description: str, detailed_description: str, knobs: List[Knob], exemplar: str, update_cadence: Optional[float], identifier: str, icons: list = ...) -> None: ...
    def async_open_popover(self, session_id: str, html: str, size) -> Coroutine[Any, Any, None]: ...
    def async_register(self, connection, coro, timeout: Optional[float] = ..., onclick: Optional[Callable[[str, Any], Coroutine[Any, Any, None]]] = ...) -> Coroutine[Any, Any, None]: ...
    def async_set_unread_count(self, session_id: Optional[str], count: int) -> Coroutine[Any, Any, None]: ...
    def set_fields_in_proto(self, proto) -> None: ...

class StringKnob:
    _StringKnob__knob: Knob
    __doc__: str
    def __init__(self, name: str, placeholder: str, default_value: str, key: str) -> None: ...
    def to_proto(self) -> Any: ...
