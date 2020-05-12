from mythril.analysis.modules.base import DetectionModule
from mythril.laser.ethereum.state.global_state import GlobalState as GlobalState
from typing import Any

log: Any
DESCRIPTION: str

def _analyze_state(state: Any): ...

class ExternalCalls(DetectionModule):
    def __init__(self) -> None: ...
    def execute(self, state: GlobalState) -> Any: ...

detector: Any
