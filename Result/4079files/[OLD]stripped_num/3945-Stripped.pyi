# (generated with --quick)

from typing import Any, List, Tuple

HttpResponse: Any
Max: Any
SingleObjectMixin: Any
SortMixin: Any
ansible: Any
consts: Any
copy: Any
core: Any
delete: Any
edit: Any
get_object_or_404: Any
inventory: Any
messages: Any
mixins: Any
modelformset_factory: Any
models: Any
os: module
redirect: Any
repeat_settings: Any
reverse: Any
reverse_lazy: Any
run: Any
search: Any
views: Any

class Copy(Any, Any):
    form_class: Any
    new_template: Any
    permission_required: str
    template_name: str
    title: str
    def form_valid(self, form) -> Any: ...
    def get_breadcrumbs(self) -> Tuple[Tuple[str, Any], Tuple[str, Any], Tuple[str, Any], Tuple[str, str]]: ...
    def get_initial(self) -> Any: ...
    def get_object(self) -> Any: ...
    def get_success_url(self) -> Any: ...

class Delete(Any, Any):
    model: Any
    permission_required: str
    success_url: Any
    template_name: str
    def get_breadcrumbs(self) -> Tuple[Tuple[str, Any], Tuple[str, Any], Tuple[str, Any], Tuple[str, str]]: ...
    def get_title(self) -> str: ...

class Edit(Any, Any, Any):
    form_class: Any
    formset_model: Any
    model: Any
    object: Any
    permission_required: str
    template_name: str
    title_create: str
    def form_valid(self, form, formset) -> Any: ...
    def get_breadcrumbs(self) -> Tuple[Tuple[str, Any], Tuple[str, Any], Tuple[Any, str]]: ...
    def get_context_data(self, *args, **kwargs) -> Any: ...
    def get_form_kwargs(self) -> Any: ...
    def get_formset_initial(self) -> Any: ...
    def get_success_url(self) -> Any: ...

class Inventory(Any, Any, Any):
    model: Any
    permission_required: str
    def get(self, *args, **kwargs) -> Any: ...

class RepeatSettings(Any, Any):
    form_class: Any
    object: Any
    permission_required: str
    template_name: str
    title: str
    def form_valid(self, form) -> Any: ...
    def get_breadcrumbs(self) -> Tuple[Tuple[str, Any], Tuple[str, Any], Tuple[str, Any], Tuple[str, str]]: ...
    def get_form_kwargs(self) -> Any: ...
    def get_success_url(self) -> Any: ...

class Run(Any, Any, Any):
    model: Any
    permission_required: str
    def get(self, request, *args, **kwargs) -> Any: ...

class Search(Any, Any, Any, Any):
    form_class: Any
    model: Any
    paginate_by: int
    permission_required: str
    sort_params: List[str]
    template_name: str
    title: str
    def get_breadcrumbs(self) -> Tuple[Tuple[str, Any], Tuple[Any, str]]: ...
    def get_paginate_by(self, queryset) -> Any: ...
    def get_queryset(self) -> Any: ...
