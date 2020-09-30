# (generated with --quick)

from typing import Any, List, Tuple

DynamicModelPermissions: Any
GeneralSerializer: Any
MODELS_TO_EXCLUDE_FROM_URL_BINDING: List[str]
apps: Any
model_name_case: Any
permissions: Any
snake_to_model_name: Any
viewsets: Any

class GeneralViewSet(Any):
    model: Any
    permission_classes: Tuple[Any, Any]
    def get_queryset(self) -> Any: ...
    def get_serializer_class(self) -> Any: ...
