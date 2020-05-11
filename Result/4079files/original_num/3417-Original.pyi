# (generated with --quick)

from typing import Any

ClientUser: Any
DjangoPermission: Any
Permission: Any
graphene: Any

class Query(Any):
    permissions: Any
    viewer: Any
    def resolve_permissions(self, info) -> Any: ...
    def resolve_viewer(self, info) -> Any: ...
