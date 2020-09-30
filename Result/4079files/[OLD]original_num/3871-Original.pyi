# (generated with --quick)

from typing import Any, Dict, Tuple, Union

bl_info: Dict[str, Union[str, Tuple[int, int, int]]]
bpy: Any
modules: Dict[str, Any]
version: Any

class SEView3DToolsPanel(Any):
    bl_category: str
    bl_context: str
    bl_label: str
    bl_region_type: str
    bl_space_type: str
    def draw(self, context) -> None: ...
    @classmethod
    def poll(self, context) -> bool: ...

def menu_func_export(self, context) -> None: ...
def register() -> None: ...
def reload(module_name) -> bool: ...
def unregister() -> None: ...
