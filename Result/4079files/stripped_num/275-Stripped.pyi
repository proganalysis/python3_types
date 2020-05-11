# (generated with --quick)

import tkinter
import tkinter.ttk
from typing import Any

__author__: str
__title__: str
__version__: str
nbt: Any
pk: Any
tk: module
ttk: module

class Menu(tkinter.Menu):
    parent: Any
    def __init__(self, parent, *args, **kwargs) -> None: ...

class NBTViewer(tkinter.Toplevel):
    file: Any
    menu: Menu
    parent: Any
    scrollbar_horizontal: tkinter.ttk.Scrollbar
    scrollbar_vertical: tkinter.ttk.Scrollbar
    statusbar: Statusbar
    toolbar: Toolbar
    widget_frame_tree: tkinter.ttk.Frame
    widget_paned_window: Any
    widget_treeview: Tree
    def __init__(self, parent, *args, **kwargs) -> None: ...
    def load_nbt(self, file = ...) -> None: ...
    def load_nested(self, parent, nbt_file, tag, compound_tag = ...) -> None: ...

class Statusbar(Any):
    status_variable: tkinter.StringVar
    def __init__(self, parent, *args) -> None: ...

class Toolbar(Any):
    parent: Any
    def __init__(self, parent, *args) -> None: ...

class Tree(tkinter.ttk.Treeview):
    parent: Any
    def __init__(self, parent, window, **kwargs) -> None: ...
    def refresh(self) -> None: ...

def main() -> None: ...
