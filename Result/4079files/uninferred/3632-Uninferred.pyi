import iterm2.util
import typing
from typing import Any

class Knob:
    __name: Any = ...
    __type: Any = ...
    __placeholder: Any = ...
    __json_default_value: Any = ...
    __key: Any = ...
    def __init__(self, type: Any, name: Any, placeholder: Any, json_default_value: Any, key: Any) -> None: ...
    def to_proto(self): ...

class CheckboxKnob:
    __knob: Any = ...
    def __init__(self, name: str, default_value: bool, key: str) -> None: ...
    def to_proto(self): ...

class StringKnob:
    __knob: Any = ...
    def __init__(self, name: str, placeholder: str, default_value: str, key: str) -> None: ...
    def to_proto(self): ...

class PositiveFloatingPointKnob:
    __knob: Any = ...
    def __init__(self, name: str, default_value: float, key: str) -> None: ...
    def to_proto(self): ...

class ColorKnob:
    __knob: Any = ...
    def __init__(self, name: str, default_value: iterm2.color.Color, key: str) -> None: ...
    def to_proto(self): ...

class StatusBarComponent:
    class Icon:
        __scale: Any = ...
        __data: Any = ...
        def __init__(self, scale: float, base64_data: str) -> None: ...
        def to_status_bar_icon(self): ...
    __short_description: Any = ...
    __detailed_description: Any = ...
    __knobs: Any = ...
    __exemplar: Any = ...
    __update_cadence: Any = ...
    __identifier: Any = ...
    __icons: Any = ...
    def __init__(self, short_description: str, detailed_description: str, knobs: typing.List[Knob], exemplar: str, update_cadence: typing.Union[float, None], identifier: str, icons: typing.List[Icon]=...) -> None: ...
    def set_fields_in_proto(self, proto: Any): ...
    async def async_open_popover(self, session_id: str, html: str, size: iterm2.util.Size) -> Any: ...
    async def async_set_unread_count(self, session_id: typing.Optional[str], count: int) -> Any: ...
    __connection: Any = ...
    async def async_register(self, connection: iterm2.connection.Connection, coro: Any, timeout: typing.Union[None, float]=..., onclick: typing.Optional[typing.Callable[[str, typing.Any], typing.Coroutine[typing.Any, typing.Any, None]]]=...) -> Any: ...