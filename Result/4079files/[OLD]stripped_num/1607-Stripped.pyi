# (generated with --quick)

import apartcore
import dialog
import partinfo
from typing import Any, Type

ApartCore: Type[apartcore.ApartCore]
Gtk: Any
OkCancelDialog: Type[dialog.OkCancelDialog]
PartitionInfo: Type[partinfo.PartitionInfo]

class RestoreFromImageEntry(Any):
    buttons: Any
    cancel_btn: Any
    core: Any
    image_entry: Any
    image_label: Any
    last_part_info: Any
    main_view: Any
    options: Any
    start_btn: Any
    title: Any
    z_options: Any
    def __init__(self, main_view, core, z_options) -> None: ...
    def on_image_select(self) -> None: ...
    def set_start_sensitivity(self) -> None: ...
    def start(self) -> None: ...
    def update_title(self) -> None: ...
    def use_defaults_for(self, part_info) -> None: ...
    def user_confirm(self) -> None: ...
