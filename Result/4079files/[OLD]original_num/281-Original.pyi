# (generated with --quick)

from typing import Any, Callable, List, Type, TypeVar

ACTION_ASSIGN: str
ACTION_REMOVE: str
ContentType: Any
Group: Any
Model: Any
ObjectPermissionChecker: Any
Permission: Any
QuerySet: Any
User: Any
assign_perm: Any
get_permission_codename: Any
remove_perm: Any

_T = TypeVar('_T')

class ObjectPermission:
    can_change: bool
    can_delete: bool
    can_view: bool
    obj: Any
    def __init__(self, obj, can_view: bool, can_change: bool, can_delete: bool) -> None: ...

def assign_permission(user_or_group, obj, perm: str) -> None: ...
@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
def get_permissions(user_or_group, object_list) -> List[ObjectPermission]: ...
def remove_permission(user_or_group, obj, perm: str) -> None: ...
def update_permission(user_or_group, obj, perm: str, action: str) -> None: ...
