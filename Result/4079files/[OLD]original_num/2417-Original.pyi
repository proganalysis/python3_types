# (generated with --quick)

from typing import Any, Callable, Dict, List

__all__: List[str]
builtin_escape_fns: Dict[str, Callable[[Any], str]]
collections: module
html: module
json: module
urllib: module

def _escape_html(unsafe_str: str) -> str: ...
def _escape_json(unsafe_var) -> str: ...
def _escape_url_with_plus(unsafe_str: str) -> str: ...
def _escape_url_without_plus(unsafe_str: str) -> str: ...
def _no_escape(unsafe_str: str) -> str: ...
