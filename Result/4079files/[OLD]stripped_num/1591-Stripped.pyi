# (generated with --quick)

from typing import Any, Dict, List, Type

Qt: Any
QtCore: Any
QtGui: Any
QtMultimedia: Any
QtWidgets: Any
datetime: Type[datetime.datetime]
path: module

class MessageArea(Any):
    chat_slot: Any
    listeners: List[nothing]
    listeners_signal: Any
    name_formats: Dict[nothing, nothing]
    sender_format: _StandardTextFormat
    sound: Any
    text_format: _StandardTextFormat
    time_format: _StandardTextFormat
    time_signal: Any
    def __init__(self, parent = ...) -> None: ...
    def _insert_and_format(self, sender, message, platform) -> None: ...
    def set_font(self, font) -> None: ...
    def set_icon(self, icon, platform) -> None: ...
    def set_settings(self, settings_model) -> None: ...

class _StandardTextFormat(Any):
    __doc__: str
    def __init__(self, text_color = ..., font = ...) -> None: ...
