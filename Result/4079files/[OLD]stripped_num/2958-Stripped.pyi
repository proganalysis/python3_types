# (generated with --quick)

import docutils.parsers.rst.states
from typing import Any, Dict, List, Pattern, Tuple, Type

ET: module
Inliner: Type[docutils.parsers.rst.states.Inliner]
link_regexp: Pattern[str]
logger: logging.Logger
logging: module
nodes: module
os: module
re: module
rst: module
set_classes: Any
signals: Any
symbol_mapping: Dict[Any, Tuple[Any, Any, Any]]
symbol_prefixes: list
tagfile_basenames: List[Tuple[Any, Any, Any]]
utils: Any

def _pelican_configure(pelicanobj) -> None: ...
def dox(name, rawtext, text, lineno, inliner, options = ..., content = ...) -> Tuple[list, List[nothing]]: ...
def init(tagfiles, input) -> None: ...
def parse_link(text) -> Tuple[str, Any, str]: ...
def register() -> None: ...
def register_mcss(mcss_settings, **kwargs) -> None: ...
