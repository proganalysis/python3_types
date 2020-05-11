# (generated with --quick)

from typing import Any

AQUIFERS_EDIT_ROLE: Any
BasePermission: Any
SAFE_METHODS: Any

class HasAquiferEditRole(Any):
    __doc__: str
    def has_permission(self, request, view) -> Any: ...

class HasAquiferEditRoleOrReadOnly(Any):
    __doc__: str
    def has_permission(self, request, view) -> Any: ...
