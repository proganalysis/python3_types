import abc
from typing import Any

class BaseSerializer(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def loads(self, data: Any, *args: Any, **kwargs: Any) -> Any: ...
    @abc.abstractmethod
    def dumps(self, data: Any, *args: Any, **kwargs: Any) -> Any: ...
