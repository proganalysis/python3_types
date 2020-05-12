from typing import Any

def build_menu(items: Any, activate: Any): ...

class GtkStatusIcon:
    _on_activate: Any = ...
    indicator: Any = ...
    _menu: Any = ...
    def __init__(self, icon_name: Any, on_activate_menu_item: Any, on_activate_status_icon: Any): ...
    def on_popup_menu(self, status_icon: Any, button: Any, activate_time: Any) -> None: ...
    def set_icon(self, icon_name: Any) -> None: ...
    def set_text(self, text: Any) -> None: ...
    def set_visibility(self, visible: Any) -> None: ...
    def set_menu(self, menu: Any) -> None: ...
