# (generated with --quick)

from typing import Any, Tuple

AllowAny: Any
PermissionDenied: Any
Player: Any
Rating: Any
Response: Any
SavedGame: Any
get_object_or_404: Any
serializers: Any
viewsets: Any

class RatingViewSet(Any):
    __doc__: str
    permission_classes: Tuple[Any]
    queryset: Any
    serializer_class: Any
    def create(self, request, *args, **kwargs) -> Any: ...
    def get_queryset(self) -> Any: ...
    def retrieve(self, request, *args, **kwargs) -> Any: ...

class SavedGameViewSet(Any):
    __doc__: str
    permission_classes: Tuple[Any]
    queryset: Any
    serializer_class: Any
    def create(self, request, *args, **kwargs) -> Any: ...
    def destroy(self, request, *args, **kwargs) -> Any: ...
    def get_queryset(self) -> Any: ...
    def retrieve(self, request, *args, **kwargs) -> Any: ...
