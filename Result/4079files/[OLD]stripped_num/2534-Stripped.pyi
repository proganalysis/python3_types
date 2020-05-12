# (generated with --quick)

from typing import Any, Dict

COMRenderer: Any
HTMLParser: Any
MarkdownParser: Any
inspect: module
parsers: Dict[str, Any]
renderers: Dict[str, Any]

def insert(operations, renderer = ..., **kwargs) -> None: ...
def parse(text, parser = ..., **kwargs) -> Any: ...
def print_operations(operations, indent_level = ...) -> None: ...
