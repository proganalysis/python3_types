# (generated with --quick)

from typing import Any

create_vex_message: Any
zmq: Any

class Messaging:
    audio_socket: Any
    publish_socket: Any
    subscribe_socket: Any
    def __init__(self, publish_address, subscribe_address, audio_publish_address) -> None: ...
    def send_audio(self, target, **contents) -> None: ...
    def send_response(self, target, **contents) -> None: ...
