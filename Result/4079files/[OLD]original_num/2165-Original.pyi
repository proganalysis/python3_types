# (generated with --quick)

import itertools
from typing import Any, Callable, Dict, Iterable, Optional, Type, TypeVar

Builder: Any
IR: Any
MotionEvent: Any
Notification: Any
ObjectProperty: Any
ScatterLayout: Any
Widget: Any
backend: Any
blocks: Any
chain: Type[itertools.chain]
logger: logging.Logger
logging: module

_S = TypeVar('_S')
_T = TypeVar('_T')

class BlackBoard(Any):
    __doc__: str
    backend: Any
    block_div: Any
    block_hashes: Dict[int, Any]
    connections: Any
    def __init__(self, **kwargs) -> None: ...
    def execute_graph(self) -> None: ...
    def get_relations(self) -> str: ...
    def in_block(self, x: float, y: float) -> Any: ...
    def on_block_executed(self, block_hash: int) -> None: ...
    def on_graph_executed(self) -> None: ...
    def on_touch_down(self, touch) -> bool: ...
    def on_touch_move(self, touch) -> bool: ...
    def on_touch_up(self, touch) -> bool: ...
    def to_ir(self) -> Any: ...

class Blocks(Any):
    __doc__: str
    def add_widget(self, widget, index: int = ..., canvas: Optional[str] = ...) -> None: ...
    def remove_widget(self, widget) -> None: ...

@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
