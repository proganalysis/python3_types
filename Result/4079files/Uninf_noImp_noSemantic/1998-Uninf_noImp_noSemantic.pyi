from src import ModuleManager
from typing import Any

EVAL_TEMPLATE: str
EVAL_URL: str

class Module(ModuleManager.BaseModule):
    _name: str = ...
    def _eval(self, lang: Any, event: Any) -> None: ...
    def eval(self, event: Any) -> None: ...
    def eval3(self, event: Any) -> None: ...