# (generated with --quick)

from typing import Any

NotificationDispatcher: Any
School: Any
json: module
logging: module
os: module
pushover: Any
sys: module

class PushoverDispatcher(Any):
    client: Any
    config: Any
    dispatcher_name: str
    logger: logging.Logger
    def __init__(self) -> None: ...
    def dispatch_notification(self, school, new_status) -> None: ...
