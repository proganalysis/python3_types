from PyQt5 import QtGui, QtWidgets
from typing import Any, Optional

class _StandardTextFormat(QtGui.QTextCharFormat):
    def __init__(self, text_color: Any = ..., font: Any = ...) -> None: ...

class MessageArea(QtWidgets.QTextEdit):
    time_signal: Any = ...
    listeners_signal: Any = ...
    sender_format: Any = ...
    time_format: Any = ...
    text_format: Any = ...
    name_formats: Any = ...
    listeners: Any = ...
    sound: Any = ...
    def __init__(self, parent: Optional[Any] = ...) -> None: ...
    def set_settings(self, settings_model: Any) -> None: ...
    def set_icon(self, icon: Any, platform: Any) -> None: ...
    def set_font(self, font: Any) -> None: ...
    def chat_slot(self, platform: Any, sender: Any, message: Any) -> None: ...
    def _insert_and_format(self, sender: Any, message: Any, platform: Any) -> None: ...
