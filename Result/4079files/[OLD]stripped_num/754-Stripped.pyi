# (generated with --quick)

import tkinter
import tkinter.ttk
from typing import Any

__author__: str
__title__: str
__version__: str
cbook: ChoiceBook
frame1: tkinter.ttk.Frame
frame2: tkinter.ttk.Frame
frame3: tkinter.ttk.Frame
i: int
root: tkinter.Tk
tk: module
ttk: module

class ChoiceBook(tkinter.ttk.Frame):
    __doc__: str
    _combobox: tkinter.ttk.Combobox
    _combobox_position: Any
    _label_list: list
    _page_list: list
    _variable: tkinter.StringVar
    frame: tkinter.ttk.Frame
    parent: Any
    def __init__(self, parent, combobox_position = ..., *args) -> None: ...
    def _change_page(self, event = ...) -> None: ...
    def add(self, child = ..., label = ...) -> None: ...
