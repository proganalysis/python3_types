# (generated with --quick)

from typing import Any, NoReturn

Author: Any
ContentType: Any
F: Any
FieldError: Any
Func: Any
HttpResponse: Any
JSONEncoder: Any
JSONField: Any
JSONRenderer: Any
JsonResponse: Any
Link: Any
Model: Any
Organization: Any
OrganizationType: Any
PublicationType: Any
QuerySet: Any
Resource: Any
Tag: Any
TemplateView: Any
Value: Any
View: Any
app_label: str
datetime: module
json: module
mark_safe: Any
render: Any

class Index(Any):
    __doc__: str
    def get(self, request, *args, **kwargs) -> Any: ...

class Lookups(Any):
    def get(self, request, *args, **kwargs) -> Any: ...

class Modified(Any):
    def get(self, request, *args, **kwargs) -> Any: ...

class ResourceList(Any):
    template_name: str
    def get_context_data(self, **kwargs) -> Any: ...

class Stats(Any):
    __doc__: str
    def get(self, request, *args, **kwargs) -> Any: ...

class Upload(Any):
    __doc__: str
    def post(self, request, *args, **kwargs) -> NoReturn: ...

def id_and_modified_times(app_label, model_label) -> Any: ...
def queryset_to_json(qs, fields) -> list: ...
def resource_mtimes(request) -> Any: ...
def resource_properties(app_label = ..., model_label = ..., since = ..., fields = ..., objects = ...) -> Any: ...
def resource_stats(as_response = ...) -> Any: ...
