# (generated with --quick)

from typing import Any, List

CFGVisitor: Any
ControlFlowGraph: Any
astroid: module

def _extract_blocks(cfg) -> List[List[str]]: ...
def _extract_edges(cfg) -> List[List[List[str]]]: ...
def build_cfgs(src: str) -> dict: ...
def test_function_with_if_and_return() -> None: ...
def test_function_with_while() -> None: ...
def test_function_with_while_if_and_return() -> None: ...
def test_multiple_simple_functions() -> None: ...
def test_simple_function() -> None: ...
def test_simple_function_with_return() -> None: ...
def test_simple_function_with_surrounding_statements() -> None: ...