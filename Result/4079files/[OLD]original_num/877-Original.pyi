# (generated with --quick)

from typing import Any, List, Optional, TypeVar

Error: Any
__all__: List[str]
collections: module
copy: module

_T1 = TypeVar('_T1')
_TTree = TypeVar('_TTree', bound=Tree)

class NotAnAstError(Any):
    __doc__: str
    instance: Any
    msg: str
    def __init__(self, instance) -> None: ...
    def __str__(self) -> str: ...

class Tree(object):
    __doc__: str
    _children: Any
    children: Any
    childrenList: type
    next: Any
    def _Tree__deepcopy(self: _TTree, memo) -> _TTree: ...
    def appendChild(self, node) -> None: ...
    def inorder(self, funct, stopOn = ...) -> Any: ...
    @classmethod
    def makenode(clss, symbol, *nexts) -> Any: ...
    def postorder(self, funct, stopOn = ...) -> Any: ...
    def preorder(self, funct, stopOn: _T1 = ...) -> Optional[_T1]: ...
    def prependChild(self, node) -> None: ...
