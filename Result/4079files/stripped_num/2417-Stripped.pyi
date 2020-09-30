# (generated with --quick)

from typing import Any, Callable, List, TypeVar

__all__: List[str]
builtin_escape_fns: collections.OrderedDict[str, Callable[[Any], Any]]
collections: module
html: module
json: module
urllib: module

_T0 = TypeVar('_T0')

def _escape_html(unsafe_str: _T0) -> _T0: ...
def _escape_json(unsafe_var) -> str: ...
def _escape_url_with_plus(unsafe_str) -> str: ...
def _escape_url_without_plus(unsafe_str) -> str: ...
def _no_escape(unsafe_str: _T0) -> _T0: ...
