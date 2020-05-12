import abc
from abc import ABC, abstractmethod

class ValidatorMixin(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def validate(self, some1: any, some2: any) -> bool: ...
