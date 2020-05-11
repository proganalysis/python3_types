# (generated with --quick)

from typing import Any, Callable, Tuple

CustomPermission: Any
permissions: Any

class IsManager(Any):
    allow_admin: bool
    object_permission_functions: Tuple[Callable[[Any, Any, Any], Any]]
    require_authentication: bool

class IsManagerOrReadOnly(Any):
    allow_read_only: bool
    object_permission_functions: Tuple[Callable[[Any, Any, Any], Any]]

class IsOrderOwnerOrAdmin(Any):
    allow_admin: bool
    allow_create: bool
    object_permission_functions: Tuple[Callable[[Any, Any, Any], Any]]
    pass_for_obj: bool
    require_authentication: bool

class IsOrderOwnerReadOnlyOrAdmin(Any):
    object_permission_functions: Tuple[Callable[[Any, Any, Any], Any]]
    permission_functions: Tuple[Callable[[Any, Any], Any]]
    require_authentication: bool

class IsOrderOwnerReadUpdateOrAdmin(Any):
    allow_admin: bool
    check_with_or: bool
    object_permission_functions: Tuple[Callable[[Any, Any, Any], Any], Callable[[Any, Any, Any], Any]]
    pass_for_obj: bool
    require_authentication: bool

def __getattr__(name) -> Any: ...
def allow_only_retrieve_for_non_admin(request, view) -> Any: ...
def check_order_ownership(request, view, obj) -> Any: ...
def no_delete(request, view, obj) -> bool: ...
def object_check_manager(request, view, obj) -> Any: ...
