# (generated with --quick)

from typing import Any, NoReturn, Tuple

BaseModule: Any
StanzaHandler: Any
app: Any
idle: Any
nbxmpp: Any

class LastActivity(Any):
    handlers: list
    def __init__(self, con) -> None: ...
    def _answer_request(self, _con, stanza, properties) -> NoReturn: ...

def get_instance(*args, **kwargs) -> Tuple[LastActivity, str]: ...
