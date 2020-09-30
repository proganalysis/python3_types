# (generated with --quick)

import collections
from typing import Any, Dict, Type

deque: Type[collections.deque]

class PropertyEvaluationContext:
    context: Dict[nothing, nothing]
    stack_of_containers: collections.deque
    def __init__(self, source_stack = ...) -> None: ...
    def popContainer(self) -> Any: ...
    def pushContainer(self, container) -> None: ...
    def rootStack(self) -> Any: ...
