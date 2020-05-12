from typing import Any, Optional

logger: Any

class DecisionsLogger:
    @staticmethod
    def debug(message_id: Any, message: str = ..., context: Optional[Any] = ..., print_log: bool = ...) -> None: ...
