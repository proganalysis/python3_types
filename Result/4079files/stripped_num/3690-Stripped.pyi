# (generated with --quick)

from typing import Any, Tuple, Type

CursorPagination: Any
GenericViewSet: Any
IsAuthenticated: Any
Notification: Any
NotificationMeta: Any
NotificationMetaSerializer: Any
NotificationSerializer: Any
Response: Any
action: Any
timezone: Any

class NotificationPagination(Any):
    ordering: str
    page_size: int

class NotificationViewSet(Any):
    __doc__: str
    mark_clicked: Any
    mark_seen: Any
    pagination_class: Type[NotificationPagination]
    permission_classes: Tuple[Any]
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...
    def list(self, request, *args, **kwargs) -> Any: ...
