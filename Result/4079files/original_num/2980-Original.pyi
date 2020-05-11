# (generated with --quick)

from typing import Any, Dict, Tuple

Chapter: Any
ChapterAdmin: Any
Module: Any
ModuleAdmin: Any
OrderedModelAdmin: Any
Section: Any
SectionAdmin: Any
StackedInline: Any
Topic: Any
TopicAdmin: Any
admin: Any
mark_safe: Any

class BaseAdmin(Any):
    prepopulated_fields: Dict[str, Tuple[str]]
    view_on_site: bool
    def page_link(self, content) -> Any: ...

class TopicInline(Any):
    extra: int
    model: Any
    ordering: Tuple[str]
    prepopulated_fields: Dict[str, Tuple[str]]
