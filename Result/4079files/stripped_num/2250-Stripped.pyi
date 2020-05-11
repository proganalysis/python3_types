# (generated with --quick)

from typing import Any, Tuple

ActivityLog: Any
Adventure: Any
AllowAny: Any
Artifact: Any
Author: Any
Effect: Any
Hint: Any
Monster: Any
Player: Any
PlayerProfile: Any
Q: Any
Response: Any
Room: Any
get_object_or_404: Any
mixins: Any
render: Any
serializers: Any
viewsets: Any

class AdventureViewSet(Any):
    __doc__: str
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...
    def retrieve(self, request, pk = ...) -> Any: ...

class ArtifactViewSet(Any):
    __doc__: str
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...

class AuthorViewSet(Any):
    __doc__: str
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...

class EffectViewSet(Any):
    __doc__: str
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...

class HintViewSet(Any):
    __doc__: str
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...

class LogViewSet(Any, Any):
    __doc__: str
    permission_classes: Tuple[Any]
    queryset: Any
    serializer_class: Any

class MonsterViewSet(Any):
    __doc__: str
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...

class PlayerProfileViewSet(Any):
    __doc__: str
    permission_classes: Tuple[Any]
    queryset: Any
    serializer_class: Any
    def create(self, request, *args, **kwargs) -> Any: ...
    def retrieve(self, request, *args, **kwargs) -> None: ...

class PlayerViewSet(Any):
    __doc__: str
    permission_classes: Tuple[Any]
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...
    def update(self, request, *args, **kwargs) -> Any: ...

class RoomViewSet(Any):
    __doc__: str
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...

def about(request) -> Any: ...
def adventure(request, slug) -> Any: ...
def adventure_list(request) -> Any: ...
def index(request, path = ...) -> Any: ...
def main_hall(request) -> Any: ...
def manual(request) -> Any: ...
def privacy_policy(request) -> Any: ...
