import abc
from abc import ABC, abstractmethod
from typing import Any

class AbsData(ABC, metaclass=abc.ABCMeta):
    driver: Any = ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, value: Any, traceback: Any) -> None: ...
    @abstractmethod
    def __iter__(self) -> Any: ...
    @abstractmethod
    def __getitem__(self, key: Any) -> Any: ...
    @abstractmethod
    def open(self) -> Any: ...
    @abstractmethod
    def close(self) -> Any: ...
    @property
    def data(self): ...
    @abstractmethod
    def __next__(self) -> Any: ...
    @abstractmethod
    def batchs_writer(self, data: Any) -> Any: ...
    @abstractmethod
    def destroy(self) -> Any: ...
    @abstractmethod
    def url(self) -> Any: ...
    @property
    @abstractmethod
    def shape(self) -> Any: ...
    @property
    @abstractmethod
    def groups(self) -> Any: ...
    @property
    @abstractmethod
    def dtypes(self) -> Any: ...
    @abstractmethod
    def to_ndarray(self) -> Any: ...