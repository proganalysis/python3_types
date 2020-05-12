from ..shared.nodes import Node
from typing import Any, Iterator

__all__: Any

def _dup(state: Node, visited: set) -> Node: ...
def dup(state: Node) -> Node: ...
def rep_range_fixed(node: Any, state: Any): ...
def rep_range_no_end(node: Any, state: Any): ...
def rep_range_with_end(node: Any, state: Any): ...
def _combine(origin_state: Node, target_state: Node, visited: set) -> None: ...
def combine(origin_state: Node, target_state: Node) -> None: ...
def nfa(nodes: Iterator[Node]) -> Node: ...
