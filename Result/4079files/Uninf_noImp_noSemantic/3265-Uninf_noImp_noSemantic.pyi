from typing import Any, List

class Writer:
    _display: Any = ...
    _delay: Any = ...
    def __init__(self, delay: int=...) -> None: ...
    def show(self, lines: List[str]) -> None: ...
    def _check_plate_input(self) -> None: ...
    def start_interactive(self, num_inputs: int=..., stop_keyword: str=...) -> None: ...
    def start_headless(self, buf: List[str]) -> None: ...
