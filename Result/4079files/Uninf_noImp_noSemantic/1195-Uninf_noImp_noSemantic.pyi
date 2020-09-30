from src import ModuleManager
from typing import Any

CAP: Any
BATCH: Any
TAG: Any

class Module(ModuleManager.BaseModule):
    def preprocess_send_privmsg(self, event: Any) -> None: ...
    def batch_end(self, event: Any): ...
