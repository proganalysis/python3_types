# (generated with --quick)

from typing import Any, Dict, Set, Tuple, Type, Union

FloatProperty: Any
IntProperty: Any
Operator: Any
Panel: Any
PointerProperty: Any
PropertyGroup: Any
Scene: Any
bl_info: Dict[str, Union[str, Tuple[int, ...]]]
bmesh: Any
bpy: Any
classes: Tuple[Type[RockBuilderPanel], Type[RockBuilderOperator], Type[RockBuilderUpdate], Type[RockGeneratorProperties]]
register_class: Any
unregister_class: Any

class RockBuilderOperator(Any):
    bl_description: str
    bl_idname: str
    bl_label: str
    bl_options: Set[str]
    def execute(self, context) -> Set[str]: ...

class RockBuilderPanel(Any):
    bl_category: str
    bl_context: str
    bl_idname: str
    bl_label: str
    bl_region_type: str
    bl_space_type: str
    def draw(self, context) -> None: ...

class RockBuilderUpdate(Any):
    bl_description: str
    bl_idname: str
    bl_label: str
    bl_options: Set[str]
    def execute(self, context) -> Set[str]: ...

class RockGeneratorProperties(Any):
    bevel_width: Any
    displace_amount: Any
    elongation: Any
    random_variation: Any
    render_subsurf: Any
    small_displace_amount: Any
    small_texture_size: Any
    texture_size: Any
    viewport_subsurf: Any

def active() -> Any: ...
def build_rock(context) -> None: ...
def displace_big() -> Any: ...
def displace_small() -> Any: ...
def random() -> float: ...
def register() -> None: ...
def setup_big_texture(text) -> None: ...
def setup_small_texture(text) -> None: ...
def unregister() -> None: ...
