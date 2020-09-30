# (generated with --quick)

from typing import Any

QQuickWidget: Any
QVBoxLayout: Any
QWidget: Any
Qt: Any
settings: Any
ui_tools: Any

class Notification(Any):
    __doc__: str
    _duration: Any
    _parent: Any
    _root: Any
    _running: bool
    _text: Any
    def __init__(self, parent = ...) -> None: ...
    def hideEvent(self, event) -> None: ...
    def set_message(self, text = ..., duration = ...) -> None: ...
    def set_parent(self, parent) -> None: ...
    def showEvent(self, event) -> None: ...
