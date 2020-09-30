# (generated with --quick)

import __future__
from typing import Any, Callable

BaseUser: Any
_BM: Any
_BManager: Any
_BQSet: Any
classproperty: Any
import_string: Any
models: Any
settings: Any
unicode_literals: __future__._Feature

class ACLModel(BModel):
    Meta: type
    acl: Any
    notes: Any
    owner: Any

class AccessExtendsFieldMixin(object):
    access_to_related: bool

class BGroupedModel(BModel):
    Meta: type
    group: Any
    parent: Any

class BModel(BaseModel):
    Meta: type
    hidden: Any
    id: Any
    def __unicode__(self) -> str: ...

class BQuerySet(Any):
    use_for_related_fields: bool
    def _BQuerySet__decorator(self, func) -> Callable: ...
    def __getattribute__(self, item) -> Any: ...
    def create(self, **kwargs) -> Any: ...
    def user_filter(self, user, *args, **kwargs) -> Any: ...

class BaseModel(Any):
    Meta: type
    acl_handler: Any
    objects: Any
    @staticmethod
    def get_acl(cls, obj = ...) -> Any: ...

class ForeignKeyACL(Any, AccessExtendsFieldMixin): ...

class ForeignKeyACLReverse(Any, ReverseAccessExtendsFieldMixin): ...

class Manager(Any):
    __doc__: str

class ManyToManyFieldACL(Any, AccessExtendsFieldMixin): ...

class ManyToManyFieldACLReverse(Any, ReverseAccessExtendsFieldMixin): ...

class ReverseAccessExtendsFieldMixin(object):
    reverse_access_to_related: bool

def first_staff_user() -> Any: ...
