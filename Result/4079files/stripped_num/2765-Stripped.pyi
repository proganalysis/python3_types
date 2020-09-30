# (generated with --quick)

from typing import Any

logging: module
sys: module
tkinter: module
zynthian_gui_config: Any

class zynthian_gui_control_xy:
    canvas: tkinter.Canvas
    height: Any
    hline: Any
    main_frame: tkinter.Frame
    padx: int
    pady: int
    shown: bool
    vline: Any
    width: Any
    x: Any
    x_zctrl: Any
    xvalue: Any
    xvalue_max: Any
    y: Any
    y_zctrl: Any
    yvalue: Any
    yvalue_max: Any
    zyngui: Any
    def __init__(self) -> None: ...
    def cb_canvas(self, event) -> None: ...
    def get_controller_values(self) -> None: ...
    def hide(self) -> None: ...
    def refresh(self) -> None: ...
    def refresh_loading(self) -> None: ...
    def set_controllers(self, x_zctrl, y_zctrl) -> None: ...
    def set_x_controller(self, x_zctrl) -> None: ...
    def set_y_controller(self, y_zctrl) -> None: ...
    def show(self) -> None: ...
    def switch_select(self, t = ...) -> None: ...
    def zyncoder_read(self) -> None: ...
