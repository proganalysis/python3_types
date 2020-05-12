# (generated with --quick)

from typing import Any

FeatureFlags: Any
Keyboards: Any
Message: Any
QtCore: Any
QtGui: Any
QtWidgets: Any
gui: Any
json: module
safe_exit: Any

class GUI(Any):
    biosignal: Any
    board: Any
    controllers: list
    keyboard_gui: Any
    layout: Any
    main_controller: Any
    setup_gui: Any
    views: Any
    def __init__(self, board, biosignal, main_controller, controllers, parent = ...) -> None: ...
    def closeEvent(self, event) -> None: ...
    def confirm_initial_setup_finished(self) -> None: ...
    def load_setup(self) -> Any: ...
    def save_setup(self, setup) -> None: ...
    def send_msg_to_controllers(self, message) -> None: ...
