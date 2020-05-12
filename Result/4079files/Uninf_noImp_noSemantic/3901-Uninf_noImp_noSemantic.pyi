from .deserializer import Deserializer
from .serializer import Serializer
from typing import Any

class StringSerializer(Serializer[str]):
    encoding: str = ...
    on_error: str = ...
    def __init__(self) -> None: ...
    def serialize(self, topic: str, data: str) -> bytes: ...
    def configure(self, configs: Any, is_key: Any) -> None: ...
    def close(self) -> None: ...

class StringDeserializer(Deserializer[str]):
    encoding: str = ...
    on_error: str = ...
    def __init__(self) -> None: ...
    def deserialize(self, topic: str, data: bytes) -> str: ...
    def configure(self, configs: Any, is_key: Any) -> None: ...
    def close(self) -> None: ...
