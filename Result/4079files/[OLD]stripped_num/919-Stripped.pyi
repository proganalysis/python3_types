# (generated with --quick)

from typing import Any, NoReturn

class SMSProviderBase:
    __doc__: str
    key: Any
    secret: Any
    def __init__(self, key, secret) -> None: ...
    def send(self, phone_numbers, message) -> NoReturn: ...
