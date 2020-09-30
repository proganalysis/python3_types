# (generated with --quick)

from typing import Any

Request: Any

class SMSEvent:
    __doc__: str
    receiver: Any
    request: Any
    sender: Any
    text_body: Any
    user_dialog: Any
    def __init__(self, request, receiver, text_body, sender, user_dialog) -> None: ...

class SMSSent(SMSEvent):
    __doc__: str
    receiver: Any
    request: Any
    sender: Any
    text_body: Any
    user_dialog: Any
