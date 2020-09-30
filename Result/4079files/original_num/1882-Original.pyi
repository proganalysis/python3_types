# (generated with --quick)

from typing import Any

DataStream: Any
GatedClockScope: Any
InputTrigger: Any
SensorGraphStatement: Any

class LatchBlock(Any):
    __doc__: str
    stream: Any
    trigger: Any
    def __init__(self, parsed, children, location = ...) -> None: ...
    def __str__(self) -> str: ...
    def execute_after(self, sensor_graph, scope_stack) -> None: ...
    def execute_before(self, sensor_graph, scope_stack) -> None: ...
