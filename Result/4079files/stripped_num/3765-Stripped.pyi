# (generated with --quick)

from typing import Any

LinkedDevices: Any
MessageCallback: Any
_LOGGER: logging.Logger
logging: module

class MockPLM:
    __doc__: str
    _message_callbacks: Any
    devices: Any
    loop: Any
    message_callbacks: Any
    sentmessage: Any
    def __init__(self, loop = ...) -> None: ...
    def message_received(self, msg) -> None: ...
    def send_msg(self, msg, wait_nak = ..., wait_timeout = ...) -> None: ...
    def start_all_linking(self, linkcode, group) -> None: ...
