# (generated with --quick)

import ssl
from typing import Any, Coroutine, Dict, Optional, Type, Union
import urllib.request

ChannelType: Any
Forbidden: Any
Image: module
ImageDraw: module
ImageFont: module
Observable: Any
Request: Type[urllib.request.Request]
asyncio: module
commands: Any
os: module

class DangerousInvite:
    baseImage: Any
    bot: Any
    errorMsg: str
    fnt: Any
    games: Dict[nothing, nothing]
    instance: Optional[DangerousInvite]
    timeOutImage: Any
    위험한초대: Any
    def __init__(self, bot) -> None: ...

class DangerousInviteGame(Any):
    bot: Any
    initChannel: Any
    initServer: Any
    initUser: Any
    isTimeOut: bool
    loop: None
    started: bool
    targetWord: Any
    def __init__(self, bot, server, user, channel) -> None: ...
    def checkStarted(self, time) -> Coroutine[Any, Any, None]: ...
    def endGame(self) -> None: ...
    def gotTargetMessage(self, message) -> Coroutine[Any, Any, None]: ...
    def start(self, word) -> Coroutine[Any, Any, None]: ...
    def timeOut(self, time) -> Coroutine[Any, Any, None]: ...
    def update(self, message) -> Coroutine[Any, Any, None]: ...

def setup(bot) -> None: ...
def urlopen(url: Union[str, urllib.request.Request], data: Optional[bytes] = ..., timeout: Optional[float] = ..., *, cafile: Optional[str] = ..., capath: Optional[str] = ..., cadefault: bool = ..., context: Optional[ssl.SSLContext] = ...) -> Any: ...
