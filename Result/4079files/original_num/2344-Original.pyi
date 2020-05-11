# (generated with --quick)

from typing import Any, List, Tuple, Union

NoReverseMatch: Any
UserActionLogEntrySubType: Any
admin: Any
escape: Any
mark_safe: Any
reverse: Any

class BaseUserActionLogEntryAdmin(Any):
    __doc__: str
    date_hierarchy: str
    list_display: List[str]
    list_filter: List[Union[str, Tuple[str, Any]]]
    readonly_fields: List[str]
    search_fields: List[str]
    def get_actions(self, request) -> Any: ...
    def has_add_permission(self, request) -> bool: ...
    def has_delete_permission(self, request, obj = ...) -> bool: ...
    def object_link(self, obj) -> Any: ...
