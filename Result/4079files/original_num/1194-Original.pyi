# (generated with --quick)

from typing import Any, Coroutine, List

CommandPlugin: Any
random: module

class MembersPlugin(Any):
    __slots__ = ["emojis", "show_offline"]
    description: List[str]
    emojis: List[str]
    show_offline: Any
    def __init__(self, *commands, prefixes = ..., strict = ..., show_offline = ...) -> None: ...
    def process_message(self, msg) -> Coroutine[Any, Any, None]: ...
    def set_description(self) -> None: ...
