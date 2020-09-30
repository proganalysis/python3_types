# (generated with --quick)

from typing import Any

Gdk: Any
Gtk: Any
ast: Any
formula: Any
os: module
solver: Any
win: Window

class Window(Any):
    fullscreen_bool: bool
    gleichungslöser: Any
    grid: Any
    lhs_Entry: Any
    lhs_ScrolledWindow: Any
    lhs_TreeView: Any
    rhs_Entry: Any
    rhs_ScrolledWindow: Any
    rhs_TreeView: Any
    separator: Any
    varsgrid: Any
    def __init__(self, g = ...) -> None: ...
    def fillTree(self) -> None: ...
    def on_gleichung_changed(self, target, param) -> None: ...
    def on_key_press(self, target, event) -> None: ...
