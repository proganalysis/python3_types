# (generated with --quick)

from typing import Any, Dict, Optional

viewsets: Any

class ModelViewSet(Any):
    @classmethod
    def get_include_map(self, include_query: str) -> Optional[Dict[str, Dict[nothing, nothing]]]: ...
    def get_queryset(self) -> Any: ...
    def get_serializer_context(self) -> dict: ...
