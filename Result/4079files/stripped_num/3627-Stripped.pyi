# (generated with --quick)

import requests.models
from typing import Any, NoReturn

req: module
settings: Any
slackweb: Any

class CustomCallbackMessenger(Messenger):
    __doc__: str
    def __init__(self) -> None: ...
    def send(self, *args, **kwargs) -> requests.models.Response: ...

class Messenger:
    __doc__: str
    def send(self, *args, **kwarg) -> NoReturn: ...

class SlackMessenger(Messenger):
    __doc__: str
    sender: Any
    def __init__(self, sender) -> None: ...
    def send(self, *args, **kwargs) -> Any: ...
