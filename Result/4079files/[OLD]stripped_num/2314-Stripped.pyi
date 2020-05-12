# (generated with --quick)

from typing import Any, Optional, TypeVar

Authentication: Any
VERSION: str
logger: logging.Logger
logging: module
requests: module

AnyStr = TypeVar('AnyStr', str, bytes)

class MoneyBird(object):
    APIError: type
    InvalidData: type
    NotFound: type
    ServerError: type
    Throttled: type
    Unauthorized: type
    __doc__: str
    authentication: Any
    base_url: str
    session: Any
    version: str
    def __init__(self, authentication) -> None: ...
    @classmethod
    def _get_url(cls, administration_id, resource_path) -> str: ...
    @staticmethod
    def _process_response(response, expected = ...) -> Any: ...
    def delete(self, resource_path, administration_id = ...) -> Any: ...
    def get(self, resource_path, administration_id = ...) -> Any: ...
    def patch(self, resource_path, data, administration_id = ...) -> Any: ...
    def post(self, resource_path, data, administration_id = ...) -> Any: ...
    def renew_session(self) -> None: ...

def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
