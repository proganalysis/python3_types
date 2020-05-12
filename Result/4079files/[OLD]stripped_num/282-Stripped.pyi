# (generated with --quick)

from typing import Any, Dict, Union

GenericClient: Any
_DEFAULT_AUTHORIZATION_TYPE: str
_DEFAULT_HTTP_METHOD: str
_DEFAULT_INTEGRATION_METHOD: str
_DEFAULT_PATH_PART: str
_DEFAULT_REQUEST_PARAMETERS: Dict[str, str]
_DEFAULT_STAGE_NAME: str
_DEFAULT_TYPE: str
logger: Any

class APIGateway(Any):
    __doc__: str
    endpoint: str
    lambda_uri: str
    uri: str
    def __init__(self, aws_properties) -> None: ...
    def _get_common_args(self, resource_info) -> Dict[str, Any]: ...
    def _get_endpoint(self) -> str: ...
    def _get_integration_args(self, resource_info) -> Dict[str, Union[str, Dict[str, str]]]: ...
    def _get_method_args(self, resource_info) -> Dict[str, Union[str, Dict[str, bool]]]: ...
    def _get_resource_id(self) -> Any: ...
    def _get_uri(self) -> str: ...
    def _set_api_gateway_id(self, api_info) -> None: ...
    def create_api_gateway(self) -> None: ...
    def delete_api_gateway(self, api_gateway_id) -> Any: ...
