# (generated with --quick)

import pathlib
from typing import Any, List, Tuple, Type

CategoryAdminForm: Any
FileDirectory: Any
HttpResponse: Any
MultipleUpload: Any
MultipleUploadForm: Any
MultipleUploadModelAdmin: Any
Path: Type[pathlib.Path]
Restore: Any
RestoreForm: Any
RestoreModelAdmin: Any
SimpleListFilter: Any
VideoCategory: Any
VideoCategoryModelAdmin: Any
VideoRegion: Any
Vod: Any
VodForm: Any
VodModelAdmin: Any
admin: Any
call_command: Any
datetime: module
django_serializers: Any
messages: Any
threading: module
uuslug: Any

class LinkModelAdmin(Any):
    list_display: List[str]
    list_editable: List[str]

class VideoFormatFilter(Any):
    parameter_name: str
    title: str
    def lookups(self, request, model_admin) -> List[Tuple[str, str]]: ...
    def queryset(self, request, queryset) -> Any: ...

def __getattr__(name) -> Any: ...
