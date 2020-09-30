# (generated with --quick)

from typing import Any

models: Any
os: module
reverse: Any
send_mail: Any
urllib: module
uuid: module

class Subscriber(Any):
    active: Any
    confirm_key: Any
    email: Any
    subscribe_date: Any
    def confirm_url(self, hostname, secure = ...) -> str: ...
    def send_subscribe_confirm_email(self) -> None: ...
