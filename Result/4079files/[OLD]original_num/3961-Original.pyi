# (generated with --quick)

from typing import Any

Request: Any

class SMSEvent:
    __doc__: str
    receiver: str
    request: Any
    sender: str
    text_body: str
    user_dialog: bool
    def __init__(self, request, receiver: str, text_body: str, sender: str, user_dialog: bool) -> None: ...

class SMSSent(SMSEvent):
    __doc__: str
    receiver: str
    request: Any
    sender: str
    text_body: str
    user_dialog: bool
