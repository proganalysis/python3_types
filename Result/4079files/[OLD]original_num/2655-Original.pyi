# (generated with --quick)

from typing import Any

FILE_ACTIONS: set
Gtk: Any
GtkSource: Any
_: Any
sys: module

class MeldFileChooserDialog(Any):
    __doc__: str
    __gtype_name__: str
    encoding_store: Any
    def __init__(self, title = ..., transient_for = ..., action = ...) -> None: ...
    def action_changed_cb(self, *args) -> None: ...
    def get_encoding(self) -> Any: ...
    def make_encoding_combo(self) -> Any: ...
