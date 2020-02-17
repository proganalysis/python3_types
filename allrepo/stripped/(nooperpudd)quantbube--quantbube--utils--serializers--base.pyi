# (generated with --quick)

from typing import Any

abc: module

class BaseSerializer(abc.ABC):
    __doc__: str
    @abstractmethod
    def dumps(self, data, *args, **kwargs) -> Any: ...
    @abstractmethod
    def loads(self, data, *args, **kwargs) -> Any: ...
