# (generated with --quick)

from typing import Any, NoReturn

BINDCODE: str
BINDSYM: str
b: Bindings
config: Any
p: Any

class Bindings:
    __doc__: str
    content: Any
    def __init__(self, content) -> None: ...
    def get_all_bindings(self) -> list: ...
    def translate_bindings(self) -> NoReturn: ...
    def write_bindings_info(self) -> NoReturn: ...
