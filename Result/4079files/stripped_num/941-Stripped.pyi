# (generated with --quick)

from typing import Any

AvatarPreferencesForm: Any
CurrentTimeZoneForm: Any
EmailForm: Any
Http404: Any
LoginForm: Any
NotificationPreferencesForm: Any
PasswordChangeForm: Any
PasswordResetForm: Any
PreferredLanguageForm: Any
UserProfile: Any
_: Any
activate: Any
auth_views: Any
get_custom_form: Any
hooks: Any
messages: Any
redirect: Any
render: Any
reverse: Any
reverse_lazy: Any
settings: Any
update_session_auth_hash: Any

class LoginView(Any):
    template_name: str
    def get(self, *args, **kwargs) -> Any: ...
    def get_context_data(self, **kwargs) -> Any: ...
    def get_form_class(self) -> Any: ...
    def get_success_url(self) -> Any: ...

class LogoutView(Any):
    next_page: str
    def dispatch(self, request, *args, **kwargs) -> Any: ...

class PasswordResetCompleteView(PasswordResetEnabledViewMixin, Any):
    template_name: str

class PasswordResetConfirmView(PasswordResetEnabledViewMixin, Any):
    success_url: Any
    template_name: str

class PasswordResetDoneView(PasswordResetEnabledViewMixin, Any):
    template_name: str

class PasswordResetEnabledViewMixin:
    __doc__: str
    def dispatch(self, *args, **kwargs) -> Any: ...

class PasswordResetView(PasswordResetEnabledViewMixin, Any):
    email_template_name: str
    form_class: Any
    subject_template_name: str
    success_url: Any
    template_name: str

def account(request) -> Any: ...
def change_avatar(request) -> Any: ...
def change_email(request) -> Any: ...
def change_password(request) -> Any: ...
def current_time_zone(request) -> Any: ...
def get_user_login_form() -> Any: ...
def language_preferences(request) -> Any: ...
def notification_preferences(request) -> Any: ...
def password_management_enabled() -> Any: ...
def password_reset_enabled() -> Any: ...
