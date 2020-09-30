# (generated with --quick)

from typing import Any

User: Any
ValidationError: Any
_: Any
forms: Any
get_user_model: Any

class UserChangeForm(Any):
    Meta: type

class UserCreationForm(Any):
    Meta: type
    error_message: Any
    def clean_username(self) -> Any: ...
