# (generated with --quick)

from typing import Any, Optional

BaseDocumentDetector: Any
wpull: Any

class XMLDetector(Any):
    @classmethod
    def is_file(cls, file) -> Optional[bool]: ...
    @classmethod
    def is_request(cls, request) -> Any: ...
    @classmethod
    def is_response(cls, response) -> Optional[bool]: ...
    @classmethod
    def is_url(cls, url_info) -> Optional[bool]: ...
