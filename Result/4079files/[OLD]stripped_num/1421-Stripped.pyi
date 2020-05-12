# (generated with --quick)

from typing import Any, Dict, Optional, Pattern, TypeVar, Union

get_text_list: Any
hook: Any
poll: Any
polls: Dict[str, Poll]
results: Any
vote: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class Poll:
    creator: Any
    options: Any
    question: Any
    voted: list
    def __init__(self, question, creator, options = ...) -> None: ...
    def format_results(self) -> str: ...
    def vote(self, voted_option, voter) -> Optional[PollOption]: ...

class PollError(Exception): ...

class PollOption:
    title: Any
    votes: int
    def __init__(self, title) -> None: ...

def findall(pattern: Union[Pattern[AnyStr], AnyStr], string: AnyStr, flags: int = ...) -> list: ...
