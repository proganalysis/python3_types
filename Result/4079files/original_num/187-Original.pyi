# (generated with --quick)

from typing import Any

Message: Any
config: Any
get_now: Any

class ChatLogger(object):
    CHANNEL: str
    LOG_QUEUE_TMPL: str
    r: Any
    def __init__(self, redis_client) -> None: ...
    def key(self, channel: str) -> str: ...
    def log(self, channel, msg) -> Any: ...
