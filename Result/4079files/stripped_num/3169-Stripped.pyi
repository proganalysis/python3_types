# (generated with --quick)

from typing import Any, Dict

CentralWidget: Any
MenuBar: Any
QtGui: Any
QtWidgets: Any
SettingsModel: Any
StatusBar: Any
glob: module
path: module

class MainWindow(Any):
    central_widget: Any
    chat_slot: Any
    command_line_signal: Any
    menu_bar: Any
    set_widget_state: Any
    settings_model: Any
    status_bar: Any
    def __init__(self, settings = ..., parent = ...) -> None: ...
    def _set_settings(self, settings) -> None: ...
    def set_command_prompt(self, prompt) -> None: ...

def _get_icon_dict() -> Dict[str, Any]: ...
