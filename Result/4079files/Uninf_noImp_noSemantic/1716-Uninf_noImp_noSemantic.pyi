import telepot
from typing import Any

likes: Any
dislikes: Any

class LentaReader(telepot.aio.helper.ChatHandler):
    keyboard: Any = ...
    _session: Any = ...
    _edit_msg_ident: Any = ...
    _editor: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def send_list(self) -> None: ...
    async def on_chat_message(self, msg: Any) -> None: ...
    async def _cancel_last(self) -> None: ...
    async def on_callback_query(self, msg: Any) -> None: ...

def main(token: Any) -> None: ...
