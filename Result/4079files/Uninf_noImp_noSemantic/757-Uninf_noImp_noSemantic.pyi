from typing import Any

class Notifications:
    GET_TOKEN: str = ...
    ITEM_ALERT: str = ...
    _session: Any = ...
    apikey: Any = ...
    token: Any = ...
    def __init__(self, username: Any, password: Any, shared_secret: Any, apikey: str = ...) -> None: ...
    @property
    def cookies(self): ...
    @staticmethod
    def gen_headers(path: Any, ref: Any, method: Any): ...
    def remove_listing_alert(self, intent: Any, item_name: Any): ...
    def add_listing_alert(self, intent: Any, type: Any, item_raw_name: Any, blanket: int = ..., craftable: bool = ...): ...