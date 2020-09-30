# (generated with --quick)

from typing import Any

Form: Any
FormDetailSerializer: Any
FormEntry: Any
FormEntrySerializer: Any
FormSerializer: Any
HttpResponse: Any
files_zip: Any
mixins: Any
viewsets: Any
write_zip: Any

class FormEntryViewSet(Any, Any):
    __doc__: str
    queryset: Any
    serializer_class: Any

class FormViewSet(Any):
    __doc__: str
    queryset: Any
    serializer_class: Any
    def get_serializer_class(self) -> Any: ...

def download_files_zip(request, form, folder) -> Any: ...
def download_multiple_forms_entries(request, forms) -> Any: ...
