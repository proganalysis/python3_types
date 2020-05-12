# (generated with --quick)

import itertools
from typing import Any, Dict, Type

AnonymousUserMixin: Any
BooleanField: Any
DateTimeField: Any
Document: Any
IntField: Any
ListField: Any
PULL: Any
ReferenceField: Any
StringField: Any
UserMixin: Any
ValidationError: Any
chain: Type[itertools.chain]
datetime: module
signals: Any

class Anonymous(Any):
    name: str

class Group(Any):
    __doc__: str
    allowed_types: Any
    description: Any
    id: Any
    meta: Dict[str, str]
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class User(Any, Any):
    __doc__: str
    active: Any
    admin: Any
    email: Any
    groups: Any
    last_login: Any
    name: Any
    password: Any
    processed: Any
    username: Any
    def __str__(self) -> str: ...
    def as_dict(self) -> Dict[str, str]: ...
    @classmethod
    def get_by_id(cls, user_id: str) -> Any: ...
    def get_stats(self, task_type) -> Dict[str, int]: ...
    def is_active(self) -> bool: ...
    def is_admin(self) -> bool: ...
    def is_eligible_for(self, task_type: str) -> bool: ...
    @classmethod
    def pre_save(cls, sender: type, document, **kwargs: dict) -> Any: ...
