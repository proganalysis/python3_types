# (generated with --quick)

from typing import Any, Callable, Dict, List, Union

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
    commands: Dict[str, Any]
    completer: Any
    display_matches: Callable[[list], None]
    keymap: Dict[str, Union[str, List[str]]]
    def __init__(self, name: str, in_stream: object, out_stream: object, err_stream: object) -> None: ...
    def _basic_completer(self, text: str) -> list: ...
    def _completer(self, text: str) -> list: ...
    def _display_matches(self, matches: list) -> None: ...
    def _run_command(self, cmd: str) -> Any: ...
    def add_command(self, tag: str, fcn) -> None: ...
    def parse_and_bind(self, cmd: str) -> None: ...
    def show_history(self, args = ...) -> None: ...
