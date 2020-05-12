# (generated with --quick)

from typing import Any

GLib: Any
GObject: Any
Gio: Any
Gtk: Any
LabeledObjectMixin: Any
MeldDoc: Any
NewDiffTab: Any
Template: Any
_: Any
enum: module
map_widgets_into_lists: Any
recent_comparisons: Any

class DiffType(enum.IntEnum):
    File: int
    Folder: int
    Unselected: int
    Version: int
    def supports_blank(self) -> bool: ...
