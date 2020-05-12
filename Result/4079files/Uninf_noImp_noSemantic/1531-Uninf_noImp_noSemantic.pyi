from docutils.parsers.rst import Directive
from docutils.transforms import Transform
from typing import Any

logger: Any
ON_RTD: Any
needs_sphinx: str
extensions: Any
project: str
copyright: str
author: str

def read_version(): ...
def read_minimum_emacs_version(): ...

release: Any
version: Any
source_suffix: str
master_doc: str
rst_prolog: Any
exclude_patterns: Any
default_role: str
primary_domain: str
templates_path: Any
pygments_style: str
nitpicky: bool
nitpick_ignore: Any
html_theme: str
html_theme_options: Any
html_sidebars: Any
html_static_path: Any
html_favicon: str
linkcheck_ignore: Any
intersphinx_mapping: Any
extlinks: Any
todo_include_todos: bool

class SupportedLanguage(Directive):
    required_arguments: int = ...
    final_argument_whitespace: bool = ...
    has_content: bool = ...
    option_spec: Any = ...
    def run(self): ...

class SyntaxCheckerConfigurationFile(Directive):
    required_arguments: int = ...
    final_argument_whitespace: bool = ...
    def run(self): ...

class IssueReferences(Transform):
    ISSUE_PATTERN: Any = ...
    ISSUE_URL_TEMPLATE: str = ...
    default_priority: int = ...
    def apply(self) -> None: ...

def build_offline_html(app: Any) -> None: ...
def add_offline_to_context(app: Any, _pagename: Any, _templatename: Any, context: Any, _doctree: Any) -> None: ...
def setup(app: Any) -> None: ...
