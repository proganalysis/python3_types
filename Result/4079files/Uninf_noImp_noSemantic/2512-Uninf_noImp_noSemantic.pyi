from bot.api.call.call import ApiCall
from bot.api.domain import Message
from bot.api.telegram import TelegramBotApi
from bot.storage import State
from typing import Any

class Api:
    telegram_api: Any = ...
    state: Any = ...
    async: Any = ...
    no_async: Any = ...
    def __init__(self, telegram_api: TelegramBotApi, state: State) -> None: ...
    def enable_async(self, async_api: Any) -> None: ...
    def send_message(self, message: Message, **params: Any) -> Any: ...
    def __should_send_message(self, message_params: Any): ...
    def __get_send_func(self, message_type: Any): ...
    def get_pending_updates(self) -> None: ...
    def get_updates(self, timeout: int = ...) -> None: ...
    def __get_updates_offset(self): ...
    def __set_updates_offset(self, last_update_id: Any) -> None: ...
    def __getattr__(self, item: Any): ...
    def __get_api_call_hook_for(self, api_call: Any): ...
    @staticmethod
    def __api_call_hook(call: ApiCall, params: dict) -> Any: ...
