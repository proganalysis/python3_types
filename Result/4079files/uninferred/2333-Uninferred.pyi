from abc import ABCMeta, abstractmethod
from typing import Any

class DataProvider(metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> Any: ...
    @staticmethod
    def calc_delay(planned: str, actual: str) -> Any: ...
