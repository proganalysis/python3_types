# (generated with --quick)

from typing import Any, Dict

BaseResponseObject: Any
objects: Any
return_key: Any

class Review(Any):
    _default_urls: Dict[str, str]
    _links: Any
    _url: str
    body: Any
    commit_id: Any
    html_url: Any
    id: Any
    state: Any
    user: Any
    @staticmethod
    def _get_key_mappings() -> Dict[str, Any]: ...
    def get_pull_request(self) -> coroutine: ...
