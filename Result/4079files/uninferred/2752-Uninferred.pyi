from PyQt5 import QtCore as QtCore, QtGui as QtGui, QtWidgets
from gui.keyboard.keyboards import Keyboards as Keyboards
from typing import Any, Optional

class GUI(QtWidgets.QWidget):
    main_controller: Any = ...
    controllers: Any = ...
    board: Any = ...
    biosignal: Any = ...
    views: Any = ...
    keyboard_gui: Any = ...
    setup_gui: Any = ...
    layout: Any = ...
    def __init__(self, board: Any, biosignal: Any, main_controller: Any, controllers: Any, parent: Optional[Any] = ...) -> None: ...
    def load_setup(self): ...
    def save_setup(self, setup: Any) -> None: ...
    def confirm_initial_setup_finished(self) -> None: ...
    def closeEvent(self, event: Any) -> None: ...
    def send_msg_to_controllers(self, message: Any) -> None: ...