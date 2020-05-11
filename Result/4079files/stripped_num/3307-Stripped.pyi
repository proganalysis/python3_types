# (generated with --quick)

import __future__
import models.base
from typing import Any, Type

ACLModel: Type[models.base.ACLModel]
BModel: Type[models.base.BModel]
BQuerySet: Type[models.base.BQuerySet]
BaseGroup: Any
BaseUser: Any
get_user_model: Any
json: module
logger: logging.Logger
logging: module
models: Any
unicode_literals: __future__._Feature

class ACLPermission(models.base.BModel):
    member: Any
    member_type: str
    role: Any
    uagroup: Any
    user: Any

class UserGroup(Any, models.base.ACLModel):
    objects: Any
    parent: Any
    users: Any

class UserSettings(models.base.BModel):
    data: Any
    settings: Any
    user: Any
    def get_settings_copy(self) -> Any: ...
