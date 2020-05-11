import graphene

from falmer.auth.types import ClientUser, Permission
from django.contrib.auth.models import Permission as DjangoPermission

class Query(graphene.ObjectType):
    viewer = graphene.Field(ClientUser)
    permissions = graphene.List(Permission)

    def resolve_viewer(self, info):
        if info.context.user.is_authenticated:
            return info.context.user
        return None

    def resolve_permissions(self, info):
        return DjangoPermission.objects.select_related('content_type').all()
