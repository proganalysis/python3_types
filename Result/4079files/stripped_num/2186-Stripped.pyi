# (generated with --quick)

import tkinter
import tkinter.ttk
from typing import Any

__author__: str
__title__: str
__version__: str
cpane: CollapsiblePane
i: int
root: tkinter.Tk
tk: module
ttk: module

class CollapsiblePane(tkinter.ttk.Frame):
    __doc__: str
    _button: tkinter.ttk.Checkbutton
    _collapsed_text: Any
    _expanded_text: Any
    _separator: tkinter.ttk.Separator
    _variable: tkinter.IntVar
    frame: tkinter.ttk.Frame
    parent: Any
    def __init__(self, parent, expanded_text = ..., collapsed_text = ..., *args) -> None: ...
    def _activate(self) -> None: ...
    def toggle(self) -> None: ...
