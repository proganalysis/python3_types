from sphinx.domains.python import PythonDomain
from typing import Any

extensions: Any
autodoc_default_options: Any
templates_path: Any
source_suffix: str
master_doc: str
project: str
copyright: str
release: Any
version: Any
exclude_patterns: Any
default_role: str
pygments_style: str
html_theme: str
html_logo: str
html_static_path: Any
htmlhelp_basename: str
latex_elements: Any
latex_documents: Any
man_pages: Any
texinfo_documents: Any

class MyPythonDomain(PythonDomain):
    def find_obj(self, env: Any, modname: Any, classname: Any, name: Any, type: Any, searchmode: int = ...): ...

def setup(sphinx: Any) -> None: ...
