# (generated with --quick)

import config
from typing import Any, Type

Configure: Type[config.Configure]

class IntranetAPI:
    __doc__: str
    _auth: None
    _config: Any
    _format: Any
    _host: Any
    def __init__(self, config) -> None: ...
    def get_config(self) -> Any: ...
    def get_format(self) -> str: ...
    def get_host(self) -> str: ...
    def set_config(self, config) -> None: ...
    def set_format(self, format) -> None: ...
    def set_host(self, host) -> None: ...
    def url_formated(self, middle) -> Any: ...
    def url_formated_with_user(self, middle, login) -> Any: ...