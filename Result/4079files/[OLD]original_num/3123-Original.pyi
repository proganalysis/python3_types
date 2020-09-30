# (generated with --quick)

import nvim_pygtk3.window
from typing import Any, List, Type, TypeVar
import uuid

GLib: Any
Gio: Any
Gtk: Any
NeovimWindow: Type[nvim_pygtk3.window.NeovimWindow]
os: module

AnyStr = TypeVar('AnyStr', str, bytes)

class NeovimApplication(Any):
    runtime: str
    scripts: List[code]
    def __init__(self, name, path, *args, **kwargs) -> None: ...
    def _configure(self, window) -> None: ...
    def do_command_line(self, command_line) -> None: ...

def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def uuid4() -> uuid.UUID: ...
