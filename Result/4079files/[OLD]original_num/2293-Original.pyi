# (generated with --quick)

from typing import Any, Tuple

Context: Any
CreateAPIView: Any
FormView: Any
GenericAPIView: Any
IsAuthenticated: Any
PREVIEW_MODE: Any
PasswordResetForm: Any
PasswordResetToken: Any
Response: Any
RetrieveAPIView: Any
UpdateAPIView: Any
authenticate: Any
get_template: Any
get_user_model: Any
login: Any
logout: Any
reverse: Any
reverse_lazy: Any
send_mail: Any
serializers: Any
settings: Any
transaction: Any
update_session_auth_hash: Any
uuid: module

class CreateAccountView(Any):
    serializer_class: Any
    def perform_create(self, serializer) -> None: ...

class LoginView(Any):
    serializer_class: Any
    def post(self, request, *args, **kwargs) -> Any: ...

class LogoutView(Any):
    def get(self, request, *args, **kwargs) -> Any: ...

class LostPasswordView(Any):
    serializer_class: Any
    def post(self, request, *args, **kwargs) -> Any: ...

class PasswordResetView(Any):
    form_class: Any
    success_url: Any
    template_name: str
    def form_valid(self, form) -> Any: ...
    def get_context_data(self, **kwargs) -> Any: ...

class UpdateEmailView(Any):
    permission_classes: Tuple[Any]
    serializer_class: Any
    def get_object(self) -> Any: ...
    def put(self, request, *args, **kwargs) -> Any: ...

class UpdatePasswordView(Any):
    permission_classes: Tuple[Any]
    serializer_class: Any
    def put(self, request, *args, **kwargs) -> Any: ...

class UserInfoView(Any):
    permission_classes: Tuple[Any]
    serializer_class: Any
    def get_object(self) -> Any: ...
