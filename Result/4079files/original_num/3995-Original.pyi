# (generated with --quick)

from typing import Any

Relocation: Any
l: logging.Logger
logging: module

class ELFReloc(Any):
    _addend: Any
    addend: Any
    is_rela: bool
    value: int
    def __init__(self, owner, symbol, relative_addr, addend = ...) -> None: ...
