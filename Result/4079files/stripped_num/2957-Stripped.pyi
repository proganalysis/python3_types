# (generated with --quick)

from typing import Any, Callable, List

ELINE: EditLine
LINE_ED: Any
_editline: Any
lineeditor: Any
os: module
sys: module

class EditLine(Any):
    IMPORTANT_VARIABLE: int
    __doc__: str
    command_token: str
    commands: dict
    completer: Any
    display_matches: Callable[[Any], Any]
    keymap: dict
    def __init__(self, name, in_stream, out_stream, err_stream) -> None: ...
    def _basic_completer(self, text) -> List[nothing]: ...
    def _completer(self, text) -> Any: ...
    def _display_matches(self, matches) -> None: ...
    def _run_command(self, cmd) -> Any: ...
    def add_command(self, tag, fcn) -> None: ...
    def parse_and_bind(self, cmd) -> None: ...
    def show_history(self, args = ...) -> None: ...
