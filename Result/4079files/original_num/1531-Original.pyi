# (generated with --quick)

import pathlib
from typing import Any, Dict, List, Pattern, Tuple, Type, Union

Directive: Any
ON_RTD: bool
Path: Type[pathlib.Path]
Transform: Any
ViewList: Any
addnodes: Any
author: str
copyright: str
default_role: str
directives: Any
exclude_patterns: List[str]
extensions: List[str]
extlinks: Dict[str, Tuple[str, str]]
html_favicon: str
html_sidebars: Dict[str, List[str]]
html_static_path: List[str]
html_theme: str
html_theme_options: Dict[str, Union[bool, str]]
intersphinx_mapping: Dict[str, Tuple[str, None]]
linkcheck_ignore: List[str]
logger: Any
logging: Any
master_doc: str
needs_sphinx: str
nitpick_ignore: List[Tuple[str, str]]
nitpicky: bool
nodes: module
os: module
primary_domain: str
process_index_entry: Any
project: str
pygments_style: str
re: module
release: str
rst_prolog: str
set_source_info: Any
source_suffix: str
sys: module
templates_path: List[str]
todo_include_todos: bool
version: str

class IssueReferences(Any):
    ISSUE_PATTERN: Pattern[str]
    ISSUE_URL_TEMPLATE: str
    default_priority: int
    def apply(self) -> None: ...

class SupportedLanguage(Any):
    final_argument_whitespace: bool
    has_content: bool
    option_spec: Dict[str, Any]
    required_arguments: int
    def run(self) -> list: ...

class SyntaxCheckerConfigurationFile(Any):
    final_argument_whitespace: bool
    required_arguments: int
    def run(self) -> Any: ...

def add_offline_to_context(app, _pagename, _templatename, context, _doctree) -> None: ...
def build_offline_html(app) -> None: ...
def read_minimum_emacs_version() -> str: ...
def read_version() -> str: ...
def setup(app) -> None: ...
