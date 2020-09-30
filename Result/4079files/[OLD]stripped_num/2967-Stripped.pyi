# (generated with --quick)

from typing import Any, Dict, Optional, Pattern, Type

gdb: Any
pretty_printers_dict: Dict[Pattern[str], Type[FlatbufferPrinter]]
re: module

class FlatbufferPrinter(object):
    __doc__: str
    size: Any
    value: Any
    vtable: Any
    def __init__(self, value) -> None: ...
    def to_string(self) -> str: ...

def build_pretty_printers_dict() -> None: ...
def lookup_function(val) -> Optional[FlatbufferPrinter]: ...
def register_printers() -> None: ...
