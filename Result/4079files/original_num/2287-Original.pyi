# (generated with --quick)

import apartcore
import partinfo
from typing import Any, List, Optional, Pattern, Type

ApartCore: Type[apartcore.ApartCore]
Gtk: Any
PartitionInfo: Type[partinfo.PartitionInfo]
invalid_name_re: Pattern[str]
re: module

class CloneToImageEntry(Any):
    buttons: Any
    cancel_btn: Any
    core: apartcore.ApartCore
    dir_entry: Any
    dir_label: Any
    last_part_info: Optional[partinfo.PartitionInfo]
    main_view: Any
    name_entry: Any
    name_label: Any
    options: Any
    start_btn: Any
    title: Any
    z_entry: Any
    z_label: Any
    def __init__(self, main_view, core: apartcore.ApartCore, z_options: List[str]) -> None: ...
    def backup_name(self) -> Any: ...
    def on_name_change(self, entry) -> None: ...
    def start_clone(self) -> None: ...
    def update_title(self, *args: None) -> None: ...
    def use_defaults_for(self, part_info: partinfo.PartitionInfo) -> None: ...
