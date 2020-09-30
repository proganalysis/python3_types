from typing import Any

extensions: Any
templates_path: Any
source_suffix: str
master_doc: str
project: str
copyright: str
author: str
__version__: Any
version: Any
release = __version__
language: Any
exclude_patterns: Any
pygments_style: str
todo_include_todos: bool
html_theme: str
html_theme_options: Any
github_url: str
autoclass_content: str
autodoc_member_order: str
autodoc_default_options: Any

def onDocstring(app: Any, what: Any, name: Any, obj: Any, options: Any, lines: Any) -> None: ...
def setup(app: Any) -> None: ...
