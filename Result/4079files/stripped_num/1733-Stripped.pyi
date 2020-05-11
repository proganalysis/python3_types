# (generated with --quick)

from typing import Any

models: Any

class Registration(Any):
    Meta: type
    __doc__: str
    email: Any
    first_name: Any
    full_name: str
    last_name: Any
    phone_number: Any
    submitted: Any
    validated: Any
    def __str__(self) -> str: ...
    @staticmethod
    def has_create_permission(request) -> bool: ...
    def has_object_read_permission(self, request) -> bool: ...
    @staticmethod
    def has_read_permission(request) -> bool: ...
