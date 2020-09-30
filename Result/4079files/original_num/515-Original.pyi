# (generated with --quick)

from typing import Any

class JsonResponse:
    json: Any
    raw_response: Any
    def __getitem__(self, name) -> Any: ...
    def __init__(self, raw_response) -> None: ...

def resolve(raw_response) -> JsonResponse: ...
