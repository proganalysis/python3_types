from dataclasses import dataclass
from typing import List, Union

from django.contrib.auth import get_permission_codename
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, QuerySet
from guardian.core import ObjectPermissionChecker
from guardian.shortcuts import assign_perm, remove_perm

from configfactory.models import User

ACTION_ASSIGN = 'assign'
ACTION_REMOVE = 'remove'


@dataclass()
class ObjectPermission:
    obj: Model
    can_view: bool
    can_change: bool
    can_delete: bool


def get_permissions(user_or_group: Union[User, Group], object_list: QuerySet) -> List[ObjectPermission]:

    permissions = []

    perm_checker = ObjectPermissionChecker(user_or_group)
    perm_checker.prefetch_perms(object_list)

    opts = object_list.model._meta

    perm_view = get_permission_codename('view', opts)
    perm_change = get_permission_codename('change', opts)
    perm_delete = get_permission_codename('delete', opts)

    for obj in object_list:
        permissions.append(
            ObjectPermission(
                obj=obj,
                can_view=perm_checker.has_perm(perm_view, obj),
                can_change=perm_checker.has_perm(perm_change, obj),
                can_delete=perm_checker.has_perm(perm_delete, obj),
            )
        )

    return permissions


def update_permission(user_or_group: Union[User, Group], obj: Model, perm: str, action: str):

    content_type = ContentType.objects.get_for_model(obj)

    # Get or create permission
    try:
        permission = Permission.objects.get(content_type=content_type, codename=perm)
    except Permission.DoesNotExist:
        name = perm.replace('_', '').title()
        permission = Permission.objects.create(
            name='Can %s %s' % (name, obj._meta.verbose_name_raw),
            content_type=content_type,
            codename=perm
        )

    if action == ACTION_ASSIGN:
        assign_perm(permission, user_or_group, obj)
    else:
        remove_perm(permission, user_or_group, obj)


def assign_permission(user_or_group: Union[User, Group], obj: Model, perm: str):
    update_permission(
        user_or_group=user_or_group,
        obj=obj,
        perm=perm,
        action=ACTION_ASSIGN
    )


def remove_permission(user_or_group: Union[User, Group], obj: Model, perm: str):
    update_permission(
        user_or_group=user_or_group,
        obj=obj,
        perm=perm,
        action=ACTION_REMOVE
    )
