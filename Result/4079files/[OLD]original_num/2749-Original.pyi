# (generated with --quick)

from typing import Any

BEHAVIORS_PLOT_COLORS: Any
CANCEL: Any
MessageDialog: Any
Ui_prefDialog: Any
logging: module
os: module

class Preferences(Any, Any):
    flag_refresh: bool
    def __init__(self, parent = ...) -> None: ...
    def browseFFmpegCacheDir(self) -> None: ...
    def refresh_preferences(self) -> None: ...
    def reset_colors(self) -> None: ...

def __getattr__(name) -> Any: ...
