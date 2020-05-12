# (generated with --quick)

from typing import Any

ProxyPlugin: Any

class Add(Any):
    INSTALLED_STATUS: str
    IN_PROGRESS_STATUS: str
    _instance: Any
    storage: None
    def __new__(cls, *args, **kwargs) -> Any: ...
    def get_api_url_key(self, command_name) -> Any: ...
    def set_name(self, api_name, status = ...) -> None: ...
    def set_url(self, api_name, url) -> None: ...
