from .models import Message as Message
from typing import Any

class ChatLogger:
    LOG_QUEUE_TMPL: Any = ...
    CHANNEL: Any = ...
    r: Any = ...
    def __init__(self, redis_client: Any) -> None: ...
    def log(self, channel: Any, msg: Message) -> Any: ...
    def key(self, channel: str) -> Any: ...
