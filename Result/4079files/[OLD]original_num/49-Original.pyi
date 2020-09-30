# (generated with --quick)

from typing import Any

BatteryUpdater: Any
QtCore: Any
QtWidgets: Any
set_icon: Any

class BatteryWidget(Any):
    _icon_label: Any
    _text_label: Any
    _updater: Any
    def __init__(self, updater, parent) -> None: ...
    def _on_update(self, percentage: float) -> None: ...
