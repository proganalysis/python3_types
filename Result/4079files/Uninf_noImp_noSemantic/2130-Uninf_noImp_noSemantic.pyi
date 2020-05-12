from ..shared import nodes
from typing import Any, Iterator, List, Optional, Tuple

__all__: Any
SYMBOLS: Any
SHORTHANDS: Any
ASSERTIONS: Any
ESCAPED_CHARS: Any
LOOKAHEAD_ASSERTIONS: Any

def parse_set(expression: Iterator[Tuple[str, str]], **kwargs: Any) -> Iterator[nodes.SetNode]: ...
def parse_repetition_range(expression: Iterator[Tuple[str, str]], **kwargs: Any) -> Iterator[nodes.RepetitionRangeNode]: ...
def parse_group_tag(expression: Iterator[Tuple[str, str]], next_char: str, **kwargs: Any) -> Iterator[nodes.GroupNode]: ...

SUB_PARSERS: Any

def _peek(iterator: Any, eof: Optional[Any] = ...): ...
def parse(expression: str) -> Iterator[nodes.Node]: ...
def greediness(expression: Iterator[nodes.Node]) -> Iterator[nodes.Node]: ...
def join_atoms(expression: Iterator[nodes.Node]) -> Iterator[nodes.Node]: ...
def fill_groups(expression: List[nodes.Node]) -> Tuple[int, dict]: ...
