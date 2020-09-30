# (generated with --quick)

from typing import Any, Set

addon_utils: Any
bpy: Any
google: module
model_pb2: Any
os: module
struct: module

class MDL_OT_exporter(Any):
    __doc__: str
    bl_idname: str
    bl_label: str
    def execute(self, context) -> Set[str]: ...
    def invoke(self, context, event) -> Set[str]: ...
    @classmethod
    def poll(cls, context) -> Any: ...
