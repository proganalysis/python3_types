# (generated with --quick)

from typing import Any, Type

CreateView: Any
Http404: Any
ListView: Any
ProblemRevisionMixin: Any
Template: Any
TemplateUpdateForm: Any
TemplateView: Any
UpdateView: Any
View: Any
datetime: Type[datetime.datetime]
get_object_or_404: Any
redirect: Any
reverse: Any
transaction: Any
transform_code_to_html: Any

class RevisionTemplateMixin(Any):
    model_class: Any
    template: Any
    def init_revision(self, *args, **kwargs) -> None: ...

class TemplateCreateView(Any, Any):
    form_class: Any
    object: Any
    polygon_title: str
    template_name: str
    def form_valid(self, form) -> Any: ...
    def get_success_url(self) -> Any: ...

class TemplateDeleteView(Any, Any):
    def post(self, request, *args, **kwargs) -> Any: ...

class TemplateList(Any, Any):
    context_object_name: str
    polygon_title: str
    template_name: str
    def get_queryset(self) -> Any: ...

class TemplatePreview(RevisionTemplateMixin, Any):
    polygon_title: str
    template_name: str
    def get_context_data(self, **kwargs) -> Any: ...

class TemplateUpdateView(RevisionTemplateMixin, Any):
    form_class: Any
    object: Any
    polygon_title: str
    template_name: str
    def form_valid(self, form) -> Any: ...
    def get_object(self, queryset = ...) -> Any: ...
    def get_success_url(self) -> Any: ...
