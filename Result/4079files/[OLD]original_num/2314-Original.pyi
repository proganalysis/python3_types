# (generated with --quick)

import requests.models
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
    def _get_url(cls, administration_id: int, resource_path: str) -> str: ...
    @staticmethod
    def _process_response(response: requests.models.Response, expected: list = ...) -> dict: ...
    def delete(self, resource_path: str, administration_id: Optional[int] = ...) -> dict: ...
    def get(self, resource_path: str, administration_id: Optional[int] = ...) -> dict: ...
    def patch(self, resource_path: str, data: dict, administration_id: Optional[int] = ...) -> dict: ...
    def post(self, resource_path: str, data: dict, administration_id: Optional[int] = ...) -> dict: ...
    def renew_session(self) -> None: ...

def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
