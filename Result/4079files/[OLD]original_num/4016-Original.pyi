# (generated with --quick)

from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar

SelectorType = Tuple[str, Optional[str]]

GraphType: str
_COMMAND_GRAPH_MAP: Dict[str, Type[CommandGraphObject]]
abc: module

_TCommandGraphNode = TypeVar('_TCommandGraphNode', bound=CommandGraphNode)

class CommandGraphCall:
    __doc__: str
    _name: str
    _parent: CommandGraphNode
    name: str
    parent: CommandGraphNode
    selectors: List[Tuple[str, Optional[str]]]
    def __init__(self, name: str, parent: CommandGraphNode) -> None: ...

class CommandGraphNode(metaclass=abc.ABCMeta):
    __doc__: str
    children: List[str]
    parent: Optional[CommandGraphNode]
    selector: Optional[str]
    selectors: List[Tuple[str, Optional[str]]]
    def call(self, name: str) -> CommandGraphCall: ...
    def navigate(self: _TCommandGraphNode, name: str, selector: Optional[str]) -> _TCommandGraphNode: ...

class CommandGraphObject(CommandGraphNode):
    __doc__: str
    _parent: CommandGraphNode
    _selector: Optional[str]
    object_type: str
    parent: CommandGraphNode
    selector: Optional[str]
    selectors: List[Tuple[str, Optional[str]]]
    def __init__(self, selector: Optional[str], parent: CommandGraphNode) -> None: ...

class CommandGraphRoot(CommandGraphNode):
    __doc__: str
    children: List[str]
    parent: None
    selector: None
    selectors: List[Tuple[str, Optional[str]]]

class _BarGraphNode(CommandGraphObject):
    _parent: CommandGraphNode
    _selector: Any
    children: List[str]
    object_type: str

class _GroupGraphNode(CommandGraphObject):
    _parent: CommandGraphNode
    _selector: Any
    children: List[str]
    object_type: str

class _LayoutGraphNode(CommandGraphObject):
    _parent: CommandGraphNode
    _selector: Any
    children: List[str]
    object_type: str

class _ScreenGraphNode(CommandGraphObject):
    _parent: CommandGraphNode
    _selector: Any
    children: List[str]
    object_type: str

class _WidgetGraphNode(CommandGraphObject):
    _parent: CommandGraphNode
    _selector: Any
    children: List[str]
    object_type: str

class _WindowGraphNode(CommandGraphObject):
    _parent: CommandGraphNode
    _selector: Any
    children: List[str]
    object_type: str
