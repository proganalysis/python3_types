# (generated with --quick)

from typing import Any, Dict, List, Optional, Tuple, Type

SelectorType = Tuple[str, Optional[str]]

GraphType: str
_COMMAND_GRAPH_MAP: Dict[str, Type[CommandGraphObject]]
abc: module

class CommandGraphCall:
    __doc__: str
    _name: Any
    _parent: Any
    name: Any
    parent: Any
    selectors: Any
    def __init__(self, name, parent) -> None: ...

class CommandGraphNode(metaclass=abc.ABCMeta):
    __doc__: str
    children: Any
    parent: Any
    selector: Any
    selectors: Any
    def call(self, name) -> CommandGraphCall: ...
    def navigate(self, name, selector) -> CommandGraphObject: ...

class CommandGraphObject(CommandGraphNode):
    __doc__: str
    _parent: Any
    _selector: Any
    object_type: Any
    parent: Any
    selector: Any
    selectors: Any
    def __init__(self, selector, parent) -> None: ...

class CommandGraphRoot(CommandGraphNode):
    __doc__: str
    children: List[str]
    parent: None
    selector: None
    selectors: List[nothing]

class _BarGraphNode(CommandGraphObject):
    _parent: Any
    _selector: Any
    children: List[str]
    object_type: str

class _GroupGraphNode(CommandGraphObject):
    _parent: Any
    _selector: Any
    children: List[str]
    object_type: str

class _LayoutGraphNode(CommandGraphObject):
    _parent: Any
    _selector: Any
    children: List[str]
    object_type: str

class _ScreenGraphNode(CommandGraphObject):
    _parent: Any
    _selector: Any
    children: List[str]
    object_type: str

class _WidgetGraphNode(CommandGraphObject):
    _parent: Any
    _selector: Any
    children: List[str]
    object_type: str

class _WindowGraphNode(CommandGraphObject):
    _parent: Any
    _selector: Any
    children: List[str]
    object_type: str
