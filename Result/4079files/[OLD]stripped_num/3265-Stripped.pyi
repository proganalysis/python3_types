# (generated with --quick)

from typing import Any

controller: module
sys: module
time: module
writer: Writer

class Writer:
    __doc__: str
    _delay: Any
    _display: controller.Display
    def __init__(self, delay = ...) -> None: ...
    def _check_plate_input(self) -> None: ...
    def show(self, lines) -> None: ...
    def start_headless(self, buf) -> Any: ...
    def start_interactive(self, num_inputs = ..., stop_keyword = ...) -> None: ...
