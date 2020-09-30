# (generated with --quick)

from typing import Any, Dict, Iterable, Optional, Union
import urllib.parse

BeautifulSoup: Any
MyFlatPages: Any
PDF_CONFIG: Dict[str, str]
PDF_TOC_CONFIG: Dict[str, str]
get_grammar: Any
path: module
pdf_folder_path: str
re: module
root_folder_path: str
subprocess: module

def generate_pdf(build_mode, pages, toc) -> str: ...
def get_pdf_content(build_mode, pages, toc) -> str: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
