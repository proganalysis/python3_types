# (generated with --quick)

import asyncio.events
import tkinter
from typing import Any

IB: Any
app: TkApp
asyncio: module
tk: module
util: Any

class TkApp:
    __doc__: str
    button: tkinter.Button
    entry: tkinter.Entry
    ib: Any
    loop: asyncio.events.AbstractEventLoop
    root: tkinter.Tk
    text: tkinter.Text
    def __init__(self) -> None: ...
    def _onDeleteWindow(self) -> None: ...
    def _onTimeout(self) -> None: ...
    def onButtonClick(self) -> None: ...
    def run(self) -> None: ...

def __getattr__(name) -> Any: ...
