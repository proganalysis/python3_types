# (generated with --quick)

from typing import Any, Dict, Set, Tuple, Union

BoolProperty: Any
ExportHelper: Any
StringProperty: Any
bl_info: Dict[str, Union[str, Tuple[int, ...]]]
bpy: Any

class CustomExportFormat(Any, Any):
    __doc__: str
    apply_modifiers: Any
    bl_idname: str
    bl_label: str
    filename_ext: str
    filter_glob: Any
    save_normal: Any
    save_tex_coord: Any
    save_vert_color: Any
    def execute(self, context) -> Set[str]: ...

def menuItemFunc_Export(self, context) -> None: ...
def register() -> None: ...
def unregister() -> None: ...
