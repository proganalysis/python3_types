from typing import Any

def correct_proxy_format(proxy: Any): ...

class Retrieve:
    USER_AGENT: str = ...
    session: Any = ...
    proxy: Any = ...
    def __init__(self, proxy: dict) -> None: ...
    def get(self, url: Any, end_cursor: str = ...): ...
    def new_proxy(self): ...
