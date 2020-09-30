# (generated with --quick)

from typing import Any

main: Any

class Callback:
    __doc__: str
    _api: Any
    chat: Any
    id: Any
    inline_message_id: Any
    isInline: bool
    message: Any
    query: Any
    sender: Any
    update: Any
    def __init__(self, update) -> None: ...
    def notify(self, text, alert = ..., cache_time = ...) -> None: ...
