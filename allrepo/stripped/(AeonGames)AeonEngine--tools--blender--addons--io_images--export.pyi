# (generated with --quick)

from typing import Any, Set

bpy: Any
os: module

class IMG_OT_exporter(Any):
    __doc__: str
    bl_idname: str
    bl_label: str
    def execute(self, context) -> Set[str]: ...
    def invoke(self, context, event) -> Set[str]: ...
    @classmethod
    def poll(cls, context) -> bool: ...
