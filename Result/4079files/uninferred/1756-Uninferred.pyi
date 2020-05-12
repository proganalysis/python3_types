from typing import Any

class Messaging:
    publish_socket: Any = ...
    subscribe_socket: Any = ...
    audio_socket: Any = ...
    def __init__(self, publish_address: str, subscribe_address: str, audio_publish_address: str) -> None: ...
    def send_response(self, target: Any, **contents: Any) -> None: ...
    def send_audio(self, target: Any, **contents: Any) -> None: ...
