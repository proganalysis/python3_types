# (generated with --quick)

import collections
import logging
import rinzler.auth.base_auth_service
import rinzler.core.response
import rinzler.core.route_mapping
import rinzler.exceptions
from typing import Any, Dict, List, Optional, Type, TypeVar

AuthException: Any
BaseAuthService: Type[rinzler.auth.base_auth_service.BaseAuthService]
HttpRequest: Any
HttpResponse: Any
Logger: Type[logging.Logger]
OrderedDict: Type[collections.OrderedDict]
RequestDataTooBig: Any
Response: Type[rinzler.core.response.Response]
RinzlerHttpException: Type[rinzler.exceptions.RinzlerHttpException]
RouteMapping: Type[rinzler.core.route_mapping.RouteMapping]
TemplateView: Any
__author__: List[str]
__version__: str
client: Any
csrf_exempt: Any
datetime: Type[datetime.datetime]
os: module
re: module
url: Any

_TRinzler = TypeVar('_TRinzler', bound=Rinzler)

class Rinzler(object):
    __doc__: str
    allowed_headers: str
    allowed_methods: str
    allowed_origins: str
    app_name: str
    auth_data: Any
    auth_service: rinzler.auth.base_auth_service.BaseAuthService
    default_headers: Dict[nothing, nothing]
    log: logging.Logger
    request_handle_time: Optional[int]
    def __init__(self, app_name: str) -> None: ...
    @staticmethod
    def get_end_point_register() -> rinzler.core.route_mapping.RouteMapping: ...
    def mount(self, route: str, controller) -> Any: ...
    def set_auth_service(self: _TRinzler, auth_service: rinzler.auth.base_auth_service.BaseAuthService) -> _TRinzler: ...
    def set_log(self: _TRinzler) -> _TRinzler: ...

class Router(Any):
    _Router__auth_service: rinzler.auth.base_auth_service.BaseAuthService
    _Router__controller: Any
    _Router__end_point_uri: str
    _Router__end_points: Dict[nothing, nothing]
    _Router__method: str
    _Router__request: Any
    _Router__request_start: datetime.datetime
    _Router__route: Any
    _Router__uri: str
    __doc__: str
    app: Rinzler
    handle: Any
    def __init__(self, app: Rinzler, route, controller) -> None: ...
    def authenticate(self, bound_route, actual_params) -> bool: ...
    @staticmethod
    def default_route_options() -> rinzler.core.response.Response: ...
    def exec_route_callback(self) -> rinzler.core.response.Response: ...
    @staticmethod
    def get_callback_pattern(expected_params, actual_params) -> dict: ...
    def get_end_point_uri(self) -> str: ...
    @staticmethod
    def get_json_ident(request_headers: dict) -> int: ...
    @staticmethod
    def get_url_params(end_point: str) -> list: ...
    def no_route_found(self, request) -> rinzler.core.response.Response: ...
    def request_matches_route(self, actual_route: str, expected_route: str) -> bool: ...
    def set_end_point_uri(self) -> bool: ...
    def set_response_headers(self, response) -> Any: ...
    def welcome_page(self) -> Any: ...

def boot(app_name) -> Rinzler: ...
def getLogger(name: Optional[str] = ...) -> logging.Logger: ...
def setup_logging(default_path = ..., env_key = ...) -> None: ...
