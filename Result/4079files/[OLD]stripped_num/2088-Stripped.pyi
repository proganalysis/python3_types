# (generated with --quick)

import abc
from typing import Any, Callable, Iterator, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
MapReduceDriver: Any
MongoDataSource: Any
logging: module
multiprocessing: module
pymongo: Any

_FuncT = TypeVar('_FuncT', bound=Callable)
_T = TypeVar('_T')

class AbstractDAO(metaclass=abc.ABCMeta):
    @abstractmethod
    def load_emblem_names(self) -> Any: ...
    @abstractmethod
    def load_songci_contents(self) -> Any: ...
    @abstractmethod
    def save_emblems_field(self, emblem_with_field_list, field_name, index) -> Any: ...

class MongoDAO(AbstractDAO):
    COLLECTION_EMBLEM: str
    COLLECTION_SONGCI_CONTENT: str
    data_source: Any
    logger: logging.Logger
    def _save_emblems_field(self, emblem_with_field_list, field_name) -> None: ...
    def load_emblem_names(self) -> list: ...
    def load_songci_contents(self) -> list: ...
    def random_emblem_name(self, where = ..., size = ...) -> Any: ...
    def save_emblems_field(self, emblem_with_field_list, field_name, index = ...) -> None: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
@overload
def repeat(object: _T) -> Iterator[_T]: ...
@overload
def repeat(object: _T, times: int) -> Iterator[_T]: ...
