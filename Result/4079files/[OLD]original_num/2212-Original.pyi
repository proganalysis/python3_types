# (generated with --quick)

from typing import Any, Coroutine, Dict, List, Set, Tuple

CommandPlugin: Any
asyncio: module
parse_user_id: Any
plural_form: Any
re: module

class VoterPlugin(Any):
    __slots__ = ["command_groups", "votes"]
    command_groups: Tuple[Any, Any, Any]
    description: List[str]
    votes: Dict[Any, Set[nothing]]
    def __init__(self, vote_commands = ..., vote_undo_commands = ..., votekick_commands = ..., prefixes = ..., strict = ...) -> None: ...
    def do_vote(self, msg, title, maximum = ..., votetime = ..., kick = ...) -> Coroutine[Any, Any, None]: ...
    def process_message(self, msg) -> coroutine: ...
