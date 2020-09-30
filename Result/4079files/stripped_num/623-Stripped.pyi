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

_T0 = TypeVar('_T0')
_TRinzler = TypeVar('_TRinzler', bound=Rinzler)

class Rinzler(object):
    __doc__: str
    allowed_headers: str
    allowed_methods: str
    allowed_origins: str
    app_name: Any
    auth_data: Dict[nothing, nothing]
    auth_service: Any
    default_headers: Dict[nothing, nothing]
    log: Optional[logging.Logger]
    request_handle_time: None
    def __init__(self, app_name) -> None: ...
    @staticmethod
    def get_end_point_register() -> rinzler.core.route_mapping.RouteMapping: ...
    def mount(self, route, controller) -> Any: ...
    def set_auth_service(self: _TRinzler, auth_service) -> _TRinzler: ...
    def set_log(self: _TRinzler) -> _TRinzler: ...

class Router(Any):
    _Router__auth_service: Any
    _Router__controller: Any
    _Router__end_point_uri: str
    _Router__end_points: Dict[nothing, nothing]
    _Router__method: str
    _Router__request: None
    _Router__request_start: None
    _Router__route: Any
    _Router__uri: str
    __doc__: str
    app: Any
    handle: Any
    def __init__(self, app, route, controller) -> None: ...
    def authenticate(self, bound_route, actual_params) -> bool: ...
    @staticmethod
    def default_route_options() -> rinzler.core.response.Response: ...
    def exec_route_callback(self) -> Any: ...
    @staticmethod
    def get_callback_pattern(expected_params, actual_params) -> dict: ...
    def get_end_point_uri(self) -> str: ...
    @staticmethod
    def get_json_ident(request_headers) -> int: ...
    @staticmethod
    def get_url_params(end_point) -> list: ...
    def no_route_found(self, request) -> rinzler.core.response.Response: ...
    def request_matches_route(self, actual_route, expected_route) -> bool: ...
    def set_end_point_uri(self) -> bool: ...
    def set_response_headers(self, response: _T0) -> _T0: ...
    def welcome_page(self) -> Any: ...

def boot(app_name) -> Rinzler: ...
def getLogger(name: Optional[str] = ...) -> logging.Logger: ...
def setup_logging(default_path = ..., env_key = ...) -> None: ...
