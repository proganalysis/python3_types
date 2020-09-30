# (generated with --quick)

import tkinter
import tkinter.ttk
from typing import Any

__author__: str
__title__: str
__version__: str
root: tkinter.Tk
tbox: ToasterBox
tk: module
ttk: module

class Popup(tkinter.ttk.Frame):
    _image: Any
    _ipad: Any
    _life: Any
    _message: Any
    _title: Any
    parent: Any
    def __init__(self, parent, title, image, message, life, height, ipad, *args) -> None: ...
    def remove(self, event = ...) -> None: ...

class ToasterBox(tkinter.Toplevel):
    __doc__: str
    _padx: Any
    _pady: Any
    _popup_fit: Any
    _popup_height: Any
    _popup_ipad: Any
    _popup_pad: Any
    _width: Any
    parent: Any
    def __init__(self, parent, width = ..., padx = ..., pady = ..., popup_fit = ..., popup_pad = ..., popup_ipad = ..., popup_height = ..., *args) -> None: ...
    def create_popup(self, title = ..., image = ..., message = ..., life = ...) -> Popup: ...
