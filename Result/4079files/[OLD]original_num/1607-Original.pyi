# (generated with --quick)

import apartcore
import dialog
import partinfo
from typing import Any, List, Optional, Type

ApartCore: Type[apartcore.ApartCore]
Gtk: Any
OkCancelDialog: Type[dialog.OkCancelDialog]
PartitionInfo: Type[partinfo.PartitionInfo]

class RestoreFromImageEntry(Any):
    buttons: Any
    cancel_btn: Any
    core: apartcore.ApartCore
    image_entry: Any
    image_label: Any
    last_part_info: Optional[partinfo.PartitionInfo]
    main_view: Any
    options: Any
    start_btn: Any
    title: Any
    z_options: List[str]
    def __init__(self, main_view, core: apartcore.ApartCore, z_options: List[str]) -> None: ...
    def on_image_select(self) -> None: ...
    def set_start_sensitivity(self) -> None: ...
    def start(self) -> None: ...
    def update_title(self) -> None: ...
    def use_defaults_for(self, part_info: partinfo.PartitionInfo) -> None: ...
    def user_confirm(self) -> None: ...
