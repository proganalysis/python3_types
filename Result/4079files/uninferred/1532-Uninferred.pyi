from overloading import __version__
from typing import Any

_projectpath: Any
extensions: Any
navtree_maxdepth: Any
source_suffix: str
source_encoding: str
master_doc: str
exclude_patterns: Any
templates_path: Any
project: str
copyright: str
author: str
_basename: str
_title: str
_subtitle: str
_project_url: str
_doc_url: str
version = __version__
release = __version__
language: str
today: str
today_fmt: str
default_role: Any
add_function_parentheses: bool
add_module_names: bool
highlight_language: str
pygments_style: str
modindex_common_prefix: Any
html_theme: str
html_theme_options: Any
html_title: Any
html_short_title = _title
_context_config: Any
html_logo: Any
html_favicon: Any
html_static_path: Any
html_extra_path: Any
html_last_updated_fmt: Any
html_use_smartypants: bool
html_add_permalinks: str
html_additional_pages: Any
html_domain_indices: bool
html_use_index: bool
html_split_index: bool
html_copy_source: bool
html_show_sourcelink: bool
html_show_sphinx: bool
html_show_copyright: bool
html_search_language: str
epub_author = author
epub_publisher = author
epub_identifier = _project_url
epub_scheme: str
epub_uid: str
epub_show_urls: str
latex_elements: Any
latex_documents: Any
latex_use_parts: bool
latex_domain_indices: bool
latex_show_urls: str
man_pages: Any
man_show_urls: bool
texinfo_documents: Any
texinfo_domain_indices: bool
texinfo_show_urls: str

def setup(app: Any) -> None: ...
def update_context(app: Any, pagename: Any, templatename: Any, context: Any, doctree: Any) -> None: ...
