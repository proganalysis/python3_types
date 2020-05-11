# (generated with --quick)

import tkinter
import tkinter.ttk
from typing import Any

__author__: str
__title__: str
__version__: str
i: int
root: tkinter.Tk
tframe: ToggledLabelFrame
tk: module
ttk: module

class ToggledLabelFrame(Any):
    __doc__: str
    _button: tkinter.ttk.Checkbutton
    _default_state: Any
    _fill: tkinter.Frame
    _off_text: Any
    _on_text: Any
    _state: Any
    _variable: tkinter.IntVar
    frame: tkinter.ttk.Frame
    parent: Any
    def __init__(self, parent, on_text = ..., off_text = ..., default_state = ..., state = ..., *args) -> None: ...
    def _activate(self) -> None: ...
    def toggle(self) -> None: ...
