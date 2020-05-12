import abc
from abc import abstractmethod
from queue import Queue
from stoq.plugins import BasePlugin

class ProviderPlugin(BasePlugin, metaclass=abc.ABCMeta):
    @abstractmethod
    def ingest(self, queue: Queue) -> None: ...
