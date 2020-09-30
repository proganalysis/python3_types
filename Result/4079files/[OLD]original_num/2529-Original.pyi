# (generated with --quick)

import http
from typing import Any, Dict, Type

BuiltinHTTPStatus: Type[http.HTTPStatus]
DateTimeFormat: str
HTTPStatus: Any
MaxContentLength: int
_http_all_attrs: Dict[str, classmethod]

class ContentTypes(object):
    FROM: Any
    JSON: Any
    MULTI_PART: Any
    TEXT: Any
    UNSUPPORTED: Any
    @classmethod
    def content_type(cls, name) -> Any: ...
    @classmethod
    def supported(cls, name) -> bool: ...

class _ContentType(object): ...
