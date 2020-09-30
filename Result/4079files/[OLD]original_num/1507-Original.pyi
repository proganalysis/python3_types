# (generated with --quick)

from typing import Any

AuthenticationForm: Any
BooleanField: Any
FormHelper: Any
ModelForm: Any
Organization: Any
User: Any
UserCreationForm: Any
autocomplete: Any
haystack: Any

class LoginForm(Any):
    helper: Any
    def __init__(self, *args, **kwargs) -> None: ...

class OrganizationForm(Any):
    Meta: type
    helper: Any
    def __init__(self, *args, editable = ..., request = ..., **kwargs) -> None: ...

class SearchForm(Any):
    def search(self) -> Any: ...

class SignUpForm(Any):
    Meta: type
    helper: Any
    terms_accepted: Any
    def __init__(self, *args, edit = ..., **kwargs) -> None: ...

class UserProfileForm(Any):
    Meta: type
    helper: Any
    def __init__(self, *args, editable = ..., request = ..., **kwargs) -> None: ...

def __getattr__(name) -> Any: ...
