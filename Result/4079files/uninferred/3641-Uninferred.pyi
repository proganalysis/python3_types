import bpy
from typing import Any

class INFO_MT_mucollider_add(bpy.types.Menu):
    bl_idname: str = ...
    bl_label: str = ...
    def draw(self, context: Any) -> None: ...

def add_collider_menu_func(self, context: Any) -> None: ...

classes_to_register: Any
menus_to_register: Any