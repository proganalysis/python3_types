from bot.action.core.action import IntermediateAction
from typing import Any

class PerChatAction(IntermediateAction):
    def process(self, event: Any) -> None: ...
