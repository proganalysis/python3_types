from django.views.generic.edit import FormView
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView, UpdateAPIView
from typing import Any

PREVIEW_MODE: Any

class CreateAccountView(CreateAPIView):
    serializer_class: Any = ...
    def perform_create(self, serializer: Any) -> None: ...

class UpdateEmailView(UpdateAPIView):
    serializer_class: Any = ...
    permission_classes: Any = ...
    def put(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_object(self): ...

class UpdatePasswordView(GenericAPIView):
    serializer_class: Any = ...
    permission_classes: Any = ...
    def put(self, request: Any, *args: Any, **kwargs: Any): ...

class LoginView(GenericAPIView):
    serializer_class: Any = ...
    def post(self, request: Any, *args: Any, **kwargs: Any): ...

class LogoutView(GenericAPIView):
    def get(self, request: Any, *args: Any, **kwargs: Any): ...

class UserInfoView(RetrieveAPIView):
    serializer_class: Any = ...
    permission_classes: Any = ...
    def get_object(self): ...

class LostPasswordView(GenericAPIView):
    serializer_class: Any = ...
    def post(self, request: Any, *args: Any, **kwargs: Any): ...

class PasswordResetView(FormView):
    template_name: str = ...
    form_class: Any = ...
    success_url: Any = ...
    def get_context_data(self, **kwargs: Any): ...
    def form_valid(self, form: Any): ...
