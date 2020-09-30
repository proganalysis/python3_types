# (generated with --quick)

from typing import Any, List, Tuple

BaseModule: Any
NetworkEvent: Any
PEPEventType: Any
app: Any
event_node: Any
nbxmpp: Any
store_publish: Any

class UserMood(Any):
    _mood_received: Any
    _nbxmpp_extends: str
    _nbxmpp_methods: List[str]
    set_mood: Any
    def __init__(self, con) -> None: ...

def get_instance(*args, **kwargs) -> Tuple[UserMood, str]: ...
