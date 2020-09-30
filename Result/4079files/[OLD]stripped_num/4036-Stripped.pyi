# (generated with --quick)

from typing import Any

ChargeSociBankAccountDeserializer: Any
CheckBalanceSerializer: Any
CustomCreateAPIView: Any
DestroyAPIView: Any
IN_QUERY: Any
ListAPIView: Any
Parameter: Any
Purchase: Any
PurchaseSerializer: Any
Response: Any
RetrieveAPIView: Any
SociBankAccount: Any
SociProduct: Any
SociProductSerializer: Any
SociSession: Any
TYPE_STRING: Any
TokenObtainSlidingView: Any
TokenRefreshSlidingView: Any
TokenVerifyView: Any
ValidationError: Any
get_object_or_404: Any
jwt: module
status: Any
swagger_auto_schema: Any
timezone: Any

class CustomTokenObtainSlidingView(Any):
    swagger_schema: None
    @staticmethod
    def _start_new_soci_session(token) -> None: ...
    def post(self, request, *args, **kwargs) -> Any: ...

class CustomTokenRefreshSlidingView(Any):
    swagger_schema: None

class CustomTokenVerifyView(Any):
    swagger_schema: None

class SociBankAccountBalanceDetailView(Any):
    __doc__: str
    get: Any
    queryset: Any
    serializer_class: Any
    def get_object(self) -> Any: ...

class SociBankAccountChargeView(Any):
    __doc__: str
    deserializer_class: Any
    lookup_url_kwarg: str
    post: Any
    queryset: Any
    serializer_class: Any

class SociProductListView(Any):
    __doc__: str
    get: Any
    queryset: Any
    serializer_class: Any

class TerminateSociSessionView(Any):
    __doc__: str
    delete: Any
