# (generated with --quick)

from typing import Any, Tuple

Model: Any
UserConfirmationRequestStatus: Any
get_random_string: Any
make_password: Any
method_connect_once: Any
random: module
string: module
utils: Any
uuid: module

class AbstractUser(Any):
    activate: Any
    change_email: Any
    delete_account: Any
    get_by_oauth_provider: Any
    get_profile: Any
    get_user_by_email: Any
    list_fields: Tuple[Any, str, str, str, str, str, str]
    on_login: Any
    patch_profile: Any
    save_oauth_info: Any
    user_profile_fields: Tuple[str, str, str, str]
    def __repr__(self) -> Any: ...
    def prepare_image(self, result = ...) -> None: ...
    @classmethod
    def set_defaults(cls, data: dict) -> None: ...

class AbstractUserActivationRequest(BaseAbstractConfirmationRequest):
    template_name: str
    def get_template_context(self) -> dict: ...

class AbstractUserChangeEmailNewAddressRequest(AbstractUserChangeEmailOriginalAddressRequest):
    send: Any
    template_name: str

class AbstractUserChangeEmailOriginalAddressRequest(BaseAbstractConfirmationRequest):
    get_by_new_email: Any
    send: Any
    template_name: str
    def get_template_context(self) -> dict: ...

class AbstractUserProfileDeleteRequest(BaseAbstractConfirmationRequest):
    template_name: str
    def get_template_context(self) -> dict: ...

class BaseAbstractConfirmationRequest(Any):
    cancel: Any
    code: str
    confirm: Any
    get_by_email: Any
    mark_as_sent: Any
    primary_key: str
    send: Any
    send_via_mailer: Any
    def get_status(self) -> Any: ...
    def is_cancelled(self) -> Any: ...
    def is_confirmed(self) -> Any: ...
    @classmethod
    def set_defaults(cls, data: dict) -> None: ...
