import abc
from typing import Any

class PublicKeySign:
    __metaclass__: Any = ...
    @abc.abstractmethod
    def sign(self, data: bytes) -> bytes: ...
