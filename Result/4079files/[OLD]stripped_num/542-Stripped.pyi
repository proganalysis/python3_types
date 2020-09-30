# (generated with --quick)

from typing import Any, List

ApprovedModel: Any
ModelAdmin: Any
_: Any
addattr: Any
render_to_string: Any

class ApprovableAdmin(Any):
    __doc__: str
    def get_object(self, request, object_id, from_field = ...) -> Any: ...

class ApprovalAdmin(Any):
    __doc__: str
    actions: List[str]
    do_approve: Any
    do_deny: Any
    get_sandbox_data: Any
    list_display: List[str]
    list_display_links: List[str]
    list_filter: List[str]
    list_select_related: bool
