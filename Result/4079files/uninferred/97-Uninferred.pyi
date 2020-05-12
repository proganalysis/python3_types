from siebenapp.domain import Graph
from typing import Any, Callable, Dict, List, Optional, Tuple

class Edge:
    BLOCKER: int = ...
    PARENT: int = ...
    __slots__: Any = ...
GoalsData = List[Tuple[int, Optional[str], bool]]
EdgesData = List[Tuple[int, int, int]]
OptionsData = List[Tuple[str, int]]

class Goals(Graph):
    goals: Any = ...
    edges: Any = ...
    closed: Any = ...
    settings: Any = ...
    events: Any = ...
    message_fn: Any = ...
    def __init__(self, name: str, message_fn: Callable[[str], None]=...) -> None: ...
    def _msg(self, message: str) -> None: ...
    def _has_link(self, lower: int, upper: int) -> bool: ...
    def _forward_edges(self, goal: int) -> List[Edge]: ...
    def _back_edges(self, goal: int) -> List[Edge]: ...
    def add(self, name: str, add_to: int=..., edge_type: int=...) -> bool: ...
    def _add_no_link(self, name: str) -> int: ...
    def select(self, goal_id: int) -> None: ...
    def hold_select(self) -> None: ...
    def q(self, keys: str=...) -> Dict[int, Any]: ...
    def _switchable(self, key: int) -> bool: ...
    def insert(self, name: str) -> None: ...
    def rename(self, new_name: str, goal_id: int=...) -> None: ...
    def toggle_close(self) -> None: ...
    def _may_be_closed(self) -> bool: ...
    def _may_be_reopened(self) -> bool: ...
    def delete(self, goal_id: int=...) -> None: ...
    def _delete(self, goal_id: int) -> None: ...
    def toggle_link(self, lower: int=..., upper: int=..., edge_type: int=...) -> None: ...
    def _replace_link(self, lower: int, upper: int, edge_type: int) -> None: ...
    def _remove_existing_link(self, lower: int, upper: int, edge_type: int=...) -> None: ...
    def _create_new_link(self, lower: int, upper: int, edge_type: int) -> None: ...
    def _transform_old_parents_into_blocked(self, lower: Any, upper: Any) -> None: ...
    def _has_circular_dependency(self, lower: int, upper: int) -> bool: ...
    def verify(self) -> bool: ...
    @staticmethod
    def build(goals: GoalsData, edges: EdgesData, settings: OptionsData, message_fn: Callable[[str], None]=...) -> Goals: ...
    @staticmethod
    def export(goals: Goals) -> Tuple[GoalsData, EdgesData, OptionsData]: ...
