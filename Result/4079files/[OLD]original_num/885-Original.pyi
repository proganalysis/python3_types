# (generated with --quick)

from typing import Any, Tuple

APIV1TokenBackPortAuthentication: Any
BasicNormalizedDataSerializer: Any
IDObfuscator: Any
Ingester: Any
JSONParser: Any
JSONRenderer: Any
ParseError: Any
ReadOnlyOrTokenHasScopeOrIsAuthenticated: Any
Response: Any
__all__: Tuple[str]
jsonschema: Any
reverse: Any
status: Any
transaction: Any
v1_schemas: Any
views: Any

class V1DataView(Any):
    __doc__: str
    authentication_classes: Tuple[Any]
    parser_classes: Tuple[Any]
    permission_classes: Tuple[Any]
    renderer_classes: Tuple[Any]
    serializer_class: Any
    def post(self, request, *args, **kwargs) -> Any: ...
