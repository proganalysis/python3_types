from typing import Any
from unshortenit.module import UnshortenModule

class AdFocus(UnshortenModule):
    name: str = ...
    domains: Any = ...
    def __init__(self, headers: dict=..., timeout: int=...) -> None: ...
    def unshorten(self, uri: str) -> str: ...
