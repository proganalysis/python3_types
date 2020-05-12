# (generated with --quick)

import enum
import json.encoder
from typing import Any, Dict, NoReturn, Optional, Tuple, Type, TypeVar, Union

Enum: Type[enum.Enum]
LOG: logging.Logger
_get_variable: Any
discord: Any
inspect: module
json: module
logging: module
pydoc: module

_T0 = TypeVar('_T0')

class AnimatedResponse(Response):
    __doc__: str
    _codeblock: str
    _content: Any
    codeblock: None
    delete_after: Any
    reply: bool
    sequence: tuple
    def __init__(self, content, *sequence, delete_after = ...) -> None: ...

class BetterLogRecord(logging.LogRecord):
    __doc__: str
    relativeCreated: float
    def __init__(self, *args, **kwargs) -> None: ...

class Response:
    __slots__ = ["_codeblock", "_content", "codeblock", "delete_after", "reply"]
    __doc__: str
    _codeblock: str
    _content: Any
    codeblock: Any
    content: Any
    delete_after: Any
    reply: Any
    def __init__(self, content, reply = ..., delete_after = ..., codeblock = ...) -> None: ...

class Serializable:
    __doc__: str
    _class_signature: Tuple[str, str, str]
    def __json__(self) -> NoReturn: ...
    @staticmethod
    def _bad(arg) -> NoReturn: ...
    @classmethod
    def _deserialize(cls, raw_json, **kwargs) -> NoReturn: ...
    def _enclose_json(self, data: _T0) -> Dict[str, Union[str, _T0]]: ...
    def serialize(self, *, cls = ..., **kwargs) -> str: ...

class Serializer(json.encoder.JSONEncoder):
    __doc__: str
    @classmethod
    def _get_vars(cls, func) -> Dict[str, Any]: ...
    @classmethod
    def deserialize(cls, data) -> Any: ...

class SkipState:
    __slots__ = ["skip_msgs", "skippers"]
    __doc__: str
    skip_count: int
    skip_msgs: set
    skippers: set
    def __init__(self) -> None: ...
    def add_skipper(self, skipper, msg) -> int: ...
    def reset(self) -> None: ...

class VoiceStateUpdate:
    __slots__ = ["after", "before", "broken"]
    Change: type
    __doc__: str
    after: Any
    before: Any
    broken: bool
    changes: list
    connecting: bool
    disconnecting: bool
    is_about_me: Any
    is_about_my_voice_channel: bool
    joining: bool
    leaving: bool
    me: Any
    member: Any
    moving: bool
    my_voice_channel: Any
    new_voice_channel: Any
    old_voice_channel: Any
    raw_change: dict
    resuming: bool
    server: Any
    voice_channel: Any
    def __init__(self, before, after) -> None: ...
    def empty(self, *, excluding_me = ..., excluding_deaf = ..., old_channel = ...) -> Optional[bool]: ...

def objdiff(obj1, obj2, *, access_attr = ..., depth = ...) -> dict: ...
