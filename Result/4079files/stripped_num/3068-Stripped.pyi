# (generated with --quick)

from typing import Any, List

AddonDialog: Any
QCheckBox: Any
QHBoxLayout: Any
QLabel: Any
QVBoxLayout: Any
Qt: Any
_: Any
create_button: Any

class StylerCheckButton(Any):
    parent: Any
    styler: Any
    def __init__(self, parent, styler) -> None: ...
    def switch_state(self, state) -> None: ...

class StylersSelectorWindow(Any):
    all_stylers: Any
    disabled_stylers: Any
    stylers_checkboxes: List[StylerCheckButton]
    stylers_layout: Any
    def __init__(self, parent, disabled_stylers, all_stylers, title = ..., on_update = ...) -> None: ...
    def check_uncheck_all(self, state) -> None: ...
    def init_ui(self, title) -> None: ...
    def on_update(self) -> Any: ...
    def update(self, styler, value) -> None: ...
