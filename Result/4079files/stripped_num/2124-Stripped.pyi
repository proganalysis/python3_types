# (generated with --quick)

from typing import Any

QCursor: Any
QEvent: Any
QMenu: Any
QMessageBox: Any
QTabBar: Any

class TabBar(Any):
    __doc__: str
    limit: Any
    menu: Any
    parent: Any
    submenu: Any
    tab_previews: bool
    def __init__(self, parent = ..., *args, **kwargs) -> None: ...
    def build_submenu(self) -> None: ...
    def eventFilter(self, obj, event) -> Any: ...
    def make_undock(self) -> Any: ...
    def mouseDoubleClickEvent(self, event) -> None: ...
    def set_position(self) -> None: ...
    def set_tab_previews(self) -> bool: ...
