# (generated with --quick)

from typing import Any

CreateView: Any
DeleteView: Any
FormView: Any
Gestalt: Any
Group: Any
HttpResponseRedirect: Any
IntegrityError: Any
PermissionMixin: Any
PermissionToken: Any
Subscription: Any
SuccessMessageMixin: Any
forms: Any
get_object_or_404: Any
info: Any
is_subscribed: Any
notifications: Any
success: Any

class GroupSubscribe(Any, Any, Any):
    already_subscribed_message: str
    form_class: Any
    group: Any
    permission_required: str
    success_message: str
    template_name: str
    def form_valid(self, form) -> Any: ...
    def get_form_kwargs(self) -> Any: ...
    def get_instance(self) -> Any: ...
    def get_permission_object(self) -> Any: ...
    def get_success_url(self) -> Any: ...
    def handle_no_permission(self) -> Any: ...

class GroupUnsubscribe(Any, Any):
    gestalt: Any
    group: Any
    model: Any
    permission_required: str
    template_name: str
    def delete(self, *args, **kwargs) -> Any: ...
    def get_object(self) -> Any: ...
    def get_permission_object(self) -> Any: ...
    def get_success_url(self) -> Any: ...

class GroupUnsubscribeConfirm(GroupUnsubscribe):
    gestalt: Any
    group: Any
    token: Any
    def has_permission(self) -> Any: ...

class GroupUnsubscribeRequest(Any, Any):
    form_class: Any
    group: Any
    permission_required: str
    template_name: str
    def form_valid(self, form) -> Any: ...
    def get_permission_object(self) -> Any: ...
    def get_success_url(self) -> Any: ...
