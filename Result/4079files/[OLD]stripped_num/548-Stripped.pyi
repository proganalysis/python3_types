# (generated with --quick)

from typing import Any, Type

datetime: Type[datetime.datetime]

class Message(object):
    date: datetime.datetime
    has_attachment: Any
    id: Any
    sender: Any
    text: Any
    title: Any
    def __init__(self, message) -> None: ...

class ReceivedMessages(list):
    def __init__(self, module_messages) -> None: ...
