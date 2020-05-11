# (generated with --quick)

import targets.target
from typing import Any, Dict, List, Type

Target: Type[targets.target.Target]

class SwitchView(targets.target.Target):
    __doc__: str
    trigger_vals: List[int]
    view_name: Any
    def __init__(self, name, parent, view) -> None: ...
    @classmethod
    def blank(cls, parent) -> Any: ...
    def serialize(self, *args, **kwargs) -> Dict[str, Any]: ...
