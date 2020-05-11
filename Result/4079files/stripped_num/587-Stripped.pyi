# (generated with --quick)

import tkinter
import tkinter.ttk
from typing import Any

__author__: str
__title__: str
__version__: str
_tkinter: Any
idlelib: Any
json: module
os: module
tk: module
ttk: module
zipfile: module

class ModDetector(tkinter.Toplevel):
    minecraft_location: Any
    minecraft_mods: Any
    parent: Any
    widget_button_cancel: Any
    widget_button_confirm: tkinter.ttk.Button
    widget_button_left: tkinter.ttk.Button
    widget_button_left_all: tkinter.ttk.Button
    widget_button_right: tkinter.ttk.Button
    widget_button_right_all: tkinter.ttk.Button
    widget_frame_buttons: tkinter.ttk.Frame
    widget_frame_buttons_bottom: tkinter.ttk.Frame
    widget_frame_main: tkinter.ttk.Frame
    widget_tree_left: Tree
    widget_tree_right: Tree
    def __init__(self, parent, *args, **kwargs) -> None: ...
    def confirm_mods(self) -> None: ...
    def exit_mod(self) -> None: ...
    def load_mcmodinfo(self, file) -> Any: ...
    def mod_search(self) -> None: ...
    def move_all_mods_left(self) -> None: ...
    def move_all_mods_right(self) -> None: ...
    def move_mod_left(self) -> None: ...
    def move_mod_right(self) -> None: ...

class Tree(tkinter.ttk.Frame):
    parent: Any
    scrollbar_horizontal: tkinter.ttk.Scrollbar
    scrollbar_vertical: tkinter.ttk.Scrollbar
    widget_tree: tkinter.ttk.Treeview
    def __init__(self, parent, **kwargs) -> None: ...

def main() -> None: ...
