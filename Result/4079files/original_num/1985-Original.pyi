# (generated with --quick)

import enhance_goodreads_export
import multiprocessing.queues
import tkinter
import tkinter.ttk
from typing import Any, Type

EnhanceExportException: Type[enhance_goodreads_export.EnhanceExportException]
multiprocessing: module
queue: module
sys: module
tk: module
ttk: module

class IOQueue(object):
    queue: queue.Queue
    def __init__(self, queue: queue.Queue) -> None: ...
    def flush(self) -> None: ...
    def write(self, text) -> None: ...

class IOText(tkinter.ttk.Frame):
    queue: multiprocessing.queues.Queue
    text: tkinter.Text
    vsb: tkinter.ttk.Scrollbar
    def __init__(self, text_queue: multiprocessing.queues.Queue, *args, **kwargs) -> None: ...
    def update(self) -> None: ...

def askopenfilename(**options) -> Any: ...
def enhance_export(options: dict) -> None: ...
def launch_gui() -> None: ...
def task(options: dict, stdout_queue: queue.Queue) -> None: ...
