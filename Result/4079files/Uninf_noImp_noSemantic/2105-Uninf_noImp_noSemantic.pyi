from abc import abstractmethod
from queue import Queue
from stoq.plugins import BasePlugin

class ProviderPlugin(BasePlugin):
    @abstractmethod
    def ingest(self, queue: Queue) -> None: ...
