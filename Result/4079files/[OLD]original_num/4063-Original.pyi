# (generated with --quick)

import asyncio.events
from typing import Any, Optional, Tuple, TypeVar, Union

BOT_TOKEN: Optional[str]
IwantRequest: Any
SUPER_TOKEN: Optional[str]
SlackCommunicator: Any
VERIFICATION: Optional[str]
_default_duration: float
_iwant_activities: Tuple[str]
_iwant_behest: Tuple[str, str]
_max_duration: float
_other_words: Tuple[str, str, str, str, str]
_slack_user_pattern: str
app: Any
asyncio: module
json: module
loop: asyncio.events.AbstractEventLoop
re: module
test1: Any
time: module
web: Any

_T = TypeVar('_T')

class TokenError(Exception): ...

def complain(what: str, iwant_object) -> dict: ...
@overload
def getenv(key: str) -> Optional[str]: ...
@overload
def getenv(key: str, default: _T) -> Union[str, _T]: ...
def handle_get(request) -> coroutine: ...
def handle_other_posts(request) -> coroutine: ...
def handle_slack_button(request) -> coroutine: ...
def handle_slack_iwant(request) -> coroutine: ...
def multidict_to_dict(multidict) -> dict: ...
def solve_iwant_activity(iwant_object) -> dict: ...
def solve_iwant_behest(iwant_object) -> dict: ...
def verify_request_token(body: dict) -> None: ...
