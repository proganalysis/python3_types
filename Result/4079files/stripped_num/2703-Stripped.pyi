# (generated with --quick)

from typing import Any

DESCRIPTION: str
DetectionModule: Any
GlobalState: Any
Issue: Any
REENTRANCY: Any
UGT: Any
UnsatError: Any
detector: ExternalCalls
json: module
log: logging.Logger
logging: module
solver: Any
symbol_factory: Any

class ExternalCalls(Any):
    __doc__: str
    def __init__(self) -> None: ...
    def execute(self, state) -> Any: ...

def _analyze_state(state) -> list: ...
