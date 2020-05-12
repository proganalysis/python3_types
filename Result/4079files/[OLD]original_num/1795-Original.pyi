# (generated with --quick)

from typing import Any, List, Tuple, Type

ActionHistory: Any
BuildGroup: Any
BuildTarget: Any
Client: Any
Playbook: Any
Project: Any
Server: Any
SortableInlineAdminMixin: Any
_: Any
admin: Any
os: module
render_to_string: Any

class BuildGroupAdmin(Any):
    Media: type
    inlines: Tuple[Type[BuildGroupTargetsTabularInline]]
    list_display: Tuple[str, str]
    def deploy(self, obj) -> Any: ...

class BuildGroupTargetsTabularInline(Any, Any):
    extra: int
    model: Any

class BuildTargetAdmin(Any):
    Media: type
    inlines: Tuple[Type[BuildTargetPlaybooksTabularInline]]
    list_display: Tuple[str, str]
    list_filter: Tuple[str, str]
    def deploy(self, obj) -> Any: ...

class BuildTargetPlaybooksTabularInline(Any, Any):
    extra: int
    model: Any

class ServerAdmin(Any):
    Media: type
    exclude: List[str]
    list_display: Tuple[str, str, str, str, str]
    readonly_fields: List[str]
    def invalidate(self, obj) -> Any: ...
