# (generated with --quick)

import BotData
from typing import Any, Optional, Type

Bot: Type[Bot.Bot]
BotBehaviors: Type[BotData.BotBehaviors]
MatchRecorder: Type[MatchRecorder.MatchRecorder]
TekkenGameState: Any

class BotFrameTrap(Bot.Bot):
    inputDelay: int
    inputDelayCode: None
    recorder: Optional[MatchRecorder.MatchRecorder]
    response: list
    def Record(self) -> None: ...
    def SetFrameTrapCommandFromNotationString(self, notation: str) -> None: ...
    def Stop(self) -> Any: ...

def ParseMoveList(moveList: str) -> list: ...
