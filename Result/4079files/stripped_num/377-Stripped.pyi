# (generated with --quick)

from typing import Any, List, Tuple

logging: module
sys: module
tkinter: module
zynautoconnect: Any
zynthian_gui_config: Any
zynthian_gui_selector: Any

class zynthian_gui_audio_out(Any):
    layer: Any
    list_data: List[Tuple[Any, Any, str]]
    def __init__(self) -> None: ...
    def back_action(self) -> str: ...
    def fill_list(self) -> None: ...
    def fill_listbox(self) -> None: ...
    def highlight(self) -> None: ...
    def select_action(self, i, t = ...) -> None: ...
    def set_layer(self, layer) -> None: ...
    def set_select_path(self) -> None: ...