# (generated with --quick)

from typing import Any

Memory: Any

class ProgramManager(object):
    _pc: Any
    isr_addr: Any
    pc: Any
    def __init__(self, isr_addr = ...) -> None: ...
    def jump(self, address) -> None: ...
    def next(self) -> None: ...
