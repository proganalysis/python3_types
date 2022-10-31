from typing import Any

class ProgramManager:
    _pc: int = ...
    isr_addr: Any = ...
    def __init__(self, isr_addr: hex=...) -> None: ...
    @property
    def pc(self) -> hex: ...
    def next(self) -> None: ...
    def jump(self, address: hex) -> Any: ...