# (generated with --quick)

import tkinter
import tkinter.ttk
from typing import Any, List, Optional, Type

__author__: str
__title__: str
__version__: str
datetime: Type[datetime.datetime]
dialog: module
functions: module
json: module
messagebox: module
mod_detector: module
os: module
pk: Any
sys: module
threading: module
tk: module
ttk: module
zipfile: module

class ProjectWindow(tkinter.Toplevel):
    included_mods: str
    minecraft_location: str
    minecraft_mods: str
    minecraft_resource_packs: str
    minecraft_versions: str
    pack_location: Optional[str]
    parent: Any
    variable_string_name: tkinter.StringVar
    variable_string_title: tkinter.StringVar
    widget_button_cancel: Any
    widget_button_create: tkinter.ttk.Button
    widget_button_detect_mods: tkinter.ttk.Button
    widget_combobox_version: tkinter.ttk.Combobox
    widget_directory_location: Any
    widget_entry_name: tkinter.ttk.Entry
    widget_entry_title: tkinter.ttk.Entry
    widget_frame_body: tkinter.ttk.Frame
    widget_frame_buttons: tkinter.ttk.Frame
    widget_label_error: tkinter.ttk.Label
    widget_text_description: tkinter.Text
    def __init__(self, parent, *args, **kwargs) -> None: ...
    def extract_minecraft_jar(self) -> None: ...
    def find_minecraft_versions(self) -> List[str]: ...
    def remove_previous_pack(self) -> None: ...

def main() -> None: ...
