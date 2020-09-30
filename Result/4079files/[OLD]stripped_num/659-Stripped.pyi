# (generated with --quick)

from typing import Any

NotifierException: Any
copy: module
logging: module
notifiers: Any
sys: module

class NotificationHandler(logging.Handler):
    __doc__: str
    defaults: Any
    fallback: Any
    fallback_defaults: Any
    provider: Any
    def __init__(self, provider, defaults = ..., **kwargs) -> None: ...
    def emit(self, record) -> None: ...
    def handleError(self, record) -> None: ...
    def init_providers(self, provider, kwargs) -> None: ...
