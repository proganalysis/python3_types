import abc
from typing import Any

class BaseSerializer(abc.ABC):
    @abc.abstractmethod
    def loads(self, data: Any, *args: Any, **kwargs: Any): ...
    @abc.abstractmethod
    def dumps(self, data: Any, *args: Any, **kwargs: Any): ...
