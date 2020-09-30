from rest_framework.permissions import BasePermission
from typing import Any

class HasAquiferEditRoleOrReadOnly(BasePermission):
    def has_permission(self, request: Any, view: Any): ...

class HasAquiferEditRole(BasePermission):
    def has_permission(self, request: Any, view: Any): ...
