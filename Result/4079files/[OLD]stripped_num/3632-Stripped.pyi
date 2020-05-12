# (generated with --quick)

from typing import Any, Coroutine

base64: module
iterm2: Any
json: module
typing: module

class CheckboxKnob:
    _CheckboxKnob__knob: Knob
    __doc__: str
    def __init__(self, name, default_value, key) -> None: ...
    def to_proto(self) -> Any: ...

class ColorKnob:
    _ColorKnob__knob: Knob
    __doc__: str
    def __init__(self, name, default_value, key) -> None: ...
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
    def __init__(self, name, default_value, key) -> None: ...
    def to_proto(self) -> Any: ...

class StatusBarComponent:
    Icon: type
    _StatusBarComponent__connection: Any
    _StatusBarComponent__detailed_description: Any
    _StatusBarComponent__exemplar: Any
    _StatusBarComponent__icons: Any
    _StatusBarComponent__identifier: Any
    _StatusBarComponent__knobs: Any
    _StatusBarComponent__short_description: Any
    _StatusBarComponent__update_cadence: Any
    __doc__: str
    def __init__(self, short_description, detailed_description, knobs, exemplar, update_cadence, identifier, icons = ...) -> None: ...
    def async_open_popover(self, session_id, html, size) -> Coroutine[Any, Any, None]: ...
    def async_register(self, connection, coro, timeout = ..., onclick = ...) -> Coroutine[Any, Any, None]: ...
    def async_set_unread_count(self, session_id, count) -> Coroutine[Any, Any, None]: ...
    def set_fields_in_proto(self, proto) -> None: ...

class StringKnob:
    _StringKnob__knob: Knob
    __doc__: str
    def __init__(self, name, placeholder, default_value, key) -> None: ...
    def to_proto(self) -> Any: ...
