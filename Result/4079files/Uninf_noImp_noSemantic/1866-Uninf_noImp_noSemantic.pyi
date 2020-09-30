from typing import Any

URLS_COLLECTION: Any
URLS_DICT: Any

def test_match_path(url: Any, path: Any, expected: Any) -> None: ...
def test_match_request(urls: Any, request_method: Any, request_path: Any, expected: Any) -> None: ...
