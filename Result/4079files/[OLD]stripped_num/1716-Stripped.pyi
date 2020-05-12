# (generated with --quick)

from typing import Any, Coroutine, Optional
import urllib.parse

BS: Any
InlineKeyboardButton: Any
InlineKeyboardMarkup: Any
MessageLoop: Any
aiohttp: Any
asyncio: module
create_open: Any
dislikes: set
include_callback_query_chat_id: Any
likes: set
pave_event_space: Any
per_chat_id: Any
sys: module
telepot: Any

class LentaReader(Any):
    _edit_msg_ident: Any
    _editor: Any
    _session: Any
    keyboard: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _cancel_last(self) -> Coroutine[Any, Any, None]: ...
    def on_callback_query(self, msg) -> Coroutine[Any, Any, None]: ...
    def on_chat_message(self, msg) -> Coroutine[Any, Any, None]: ...
    def send_list(self) -> Coroutine[Any, Any, None]: ...

def main(token) -> None: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
