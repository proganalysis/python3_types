from gi.repository import Gtk
from mathx.gui.AstTree import ast as ast
from typing import Any, Optional

class Window(Gtk.Window):
    fullscreen_bool: bool = ...
    gleichungslöser: Any = ...
    grid: Any = ...
    lhs_Entry: Any = ...
    lhs_ScrolledWindow: Any = ...
    lhs_TreeView: Any = ...
    separator: Any = ...
    rhs_Entry: Any = ...
    rhs_ScrolledWindow: Any = ...
    rhs_TreeView: Any = ...
    varsgrid: Any = ...
    def __init__(self, g: Optional[Any] = ...) -> None: ...
    def on_key_press(self, target: Any, event: Any) -> None: ...
    def on_gleichung_changed(self, target: Any, param: Any) -> None: ...
    def fillTree(self) -> None: ...
