# (generated with --quick)

from typing import Any, Dict

ACTIVATION_TYPES: Dict[str, str]
User: Any
ValidationError: Any
_: Any
clean_for_user_description: Any
markdown: Any
models: Any
sensitive_variables: Any

class Activation(Any):
    token: Any
    type: Any
    user: Any

class Faculty(Any):
    name: Any
    def __str__(self) -> Any: ...

class StudentInformation(UserInformation):
    faculty: Any
    s_number: Any
    verified: Any
    def make_zih_mail(self) -> Any: ...

class UserInformation(Any):
    accepted_privacy_policy: Any
    description: Any
    public_profile: Any
    user: Any
    def __str__(self) -> str: ...
    @staticmethod
    def create(username, email, password, first_name, last_name, s_number = ..., faculty = ...) -> Any: ...
    def is_pending_student(self) -> bool: ...
    def is_student(self) -> bool: ...
    def is_verified_student(self) -> Any: ...
    def render_description(self) -> Any: ...

def get_user_information(obj) -> Any: ...
def privacy_policy_consented(consented) -> None: ...
