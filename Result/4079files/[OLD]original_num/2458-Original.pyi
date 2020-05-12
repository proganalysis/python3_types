# (generated with --quick)

from typing import Any

DCOSException: Any

class Decoder(object):
    FAILED: int
    HEADER: int
    RECORD: int
    __doc__: str
    buffer: bytes
    length: int
    state: int
    def __init__(self, deserialize) -> None: ...
    def decode(self, data) -> list: ...
    def deserialize(self, _1: bytes) -> Any: ...

class Encoder(object):
    __doc__: str
    def __init__(self, serialize) -> None: ...
    def encode(self, message) -> bytes: ...
    def serialize(self, _1) -> Any: ...
