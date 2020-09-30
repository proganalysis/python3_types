# (generated with --quick)

import tkinter
import tkinter.ttk
from typing import Any

__author__: str
__title__: str
__version__: str
button: Any
pentry: PasswordEntry
root: tkinter.Tk
tk: module
ttk: module

class PasswordEntry(tkinter.ttk.Entry):
    __doc__: str
    _cover_character: Any
    _entry_text: list
    parent: Any
    def __init__(self, parent, cover_character = ..., *args) -> None: ...
    def _delete_last(self, event = ...) -> None: ...
    def _update_text(self, *args) -> None: ...
    def get_text(self) -> str: ...
