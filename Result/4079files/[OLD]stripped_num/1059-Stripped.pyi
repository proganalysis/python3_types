# (generated with --quick)

import threading
import tkinter
import tkinter.ttk
from typing import Any, Optional, Type

IMAGE_QUALITY: int
Image: module
MAX_SPEED: int
Thread: Type[threading.Thread]
__author__: str
__version__: str
os: module
tk: module
ttk: module

class MainApp(object):
    btn_input: tkinter.ttk.Button
    btn_output: tkinter.ttk.Button
    btn_start: tkinter.ttk.Button
    file_output: Any
    files: list
    frame_footer: tkinter.Frame
    frame_main: tkinter.Frame
    label_speed: tkinter.ttk.Label
    label_title: tkinter.ttk.Label
    label_version: tkinter.Label
    master: Any
    progress_bar: tkinter.ttk.Progressbar
    rolling_shutter: Optional[RollingShutter]
    speed_scale: tkinter.ttk.Scale
    tk_progress_val: tkinter.DoubleVar
    tk_speed_val: tkinter.IntVar
    def __init__(self, master) -> None: ...
    def disable_buttons(self) -> None: ...
    def enable_buttons(self) -> None: ...
    def on_closing(self) -> None: ...
    def select_input(self) -> None: ...
    def select_output(self) -> None: ...
    def start(self) -> None: ...
    def update_progress(self, value) -> None: ...
    def update_speed(self, event = ...) -> None: ...

class RollingShutter(object):
    current_row: Any
    frame_count: int
    frame_paths: Any
    height: Any
    img_output: Any
    path_output: Any
    running: bool
    speed: Any
    width: Any
    def __init__(self, frame_paths, speed, path_output) -> None: ...
    def thread(self, app_obj) -> None: ...

def askopenfile(mode: str = ..., **options) -> Any: ...
def asksaveasfilename(**options) -> Any: ...
def askyesno(title: Optional[str] = ..., message: Optional[str] = ..., **options) -> bool: ...
def main() -> None: ...
def showerror(title: Optional[str] = ..., message: Optional[str] = ..., **options) -> str: ...
def showinfo(title: Optional[str] = ..., message: Optional[str] = ..., **options) -> str: ...
