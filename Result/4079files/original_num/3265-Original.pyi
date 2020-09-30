# (generated with --quick)

from typing import List

controller: module
sys: module
time: module
writer: Writer

class Writer:
    __doc__: str
    _delay: int
    _display: controller.Display
    def __init__(self, delay: int = ...) -> None: ...
    def _check_plate_input(self) -> None: ...
    def show(self, lines: List[str]) -> None: ...
    def start_headless(self, buf: List[str]) -> None: ...
    def start_interactive(self, num_inputs: int = ..., stop_keyword: str = ...) -> None: ...
