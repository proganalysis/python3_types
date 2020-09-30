from configfactory.models import User as User
from django.contrib.auth.models import Group as Group
from django.db.models import Model, QuerySet
from typing import Any, List, Union

ACTION_ASSIGN: str
ACTION_REMOVE: str

class ObjectPermission:
    obj: Model
    can_view: bool
    can_change: bool
    can_delete: bool

def get_permissions(user_or_group: Union[User, Group], object_list: QuerySet) -> List[ObjectPermission]: ...
def update_permission(user_or_group: Union[User, Group], obj: Model, perm: str, action: str) -> Any: ...
def assign_permission(user_or_group: Union[User, Group], obj: Model, perm: str) -> Any: ...
def remove_permission(user_or_group: Union[User, Group], obj: Model, perm: str) -> Any: ...
