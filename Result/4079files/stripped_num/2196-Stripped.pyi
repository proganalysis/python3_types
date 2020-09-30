# (generated with --quick)

from typing import Any, Dict, Tuple, Type

Album: Any
Photo: Any
Video: Any
admin: Any
forms: Any
re: module
youtube_video_id: Any

class VideoAddForm(Any):
    Meta: type
    link: Any
    def clean_link(self) -> Any: ...
    def save(self, commit = ...) -> Any: ...

class VideoAdmin(Any):
    add_fieldsets: Tuple[Tuple[None, Dict[str, Tuple[str, ...]]]]
    add_form: Type[VideoAddForm]
    fieldsets: Tuple[Tuple[None, Dict[str, Tuple[str, str, str, str, str, str, str]]], Tuple[str, Dict[str, Tuple[str, ...]]]]
    list_display: Tuple[str, str, str, str, str, str, str, str]
    list_filter: Tuple[str, str, str, str, str]
    ordering: Tuple[str]
    search_fields: Tuple[str]
    def get_fieldsets(self, request, obj = ...) -> Any: ...
    def get_form(self, request, obj = ..., **kwargs) -> Any: ...
