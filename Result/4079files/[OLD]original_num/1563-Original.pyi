# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, Callable, Dict, Iterable, List, Optional, TextIO, Type, TypeVar, Union
import urllib.parse

BeautifulSoup: Any
DateAwareEncoder: Any
Feature: Any
Flask: Type[flask.app.Flask]
Freezer: Any
MyFlatPages: Any
Response: Type[flask.wrappers.Response]
_nav_cache: Any
_nav_lock: threading._RLock
add_data_to_context: Any
add_header: Callable[[flask.wrappers.Response], flask.wrappers.Response]
add_year_to_context: Any
api_page: Callable
app: flask.app.Flask
arg: str
argv_copy: List[str]
assert_valid_git_hub_url: Any
asset: Any
books_page: Callable
build_check_links: bool
build_contenteditable: bool
build_errors: List[str]
build_mode: bool
build_search_indices: Any
collections_redirect: Callable
community_page: Callable
community_redirect: Callable
community_user_groups_redirect: Callable
compatibility_redirect: Callable
copy: module
coroutines_redirect: Callable
coroutines_tutor_redirect: Callable
data_folder: str
datetime: module
error: Any
events_redirect: Callable
freezer: Any
generate_sitemap: Any
get_api_page: Any
get_cities: Callable
get_events: Callable
get_grammar: Any
get_index_page: Callable
glob: module
grammar: Callable
ignore_stdlib: bool
index_page: Callable
jinja_aware_markdown: Any
json: module
os: module
output: TextIO
page: Callable
page_404: Callable
page_not_found: Callable
pages: Any
path: module
pdf: Callable
process_code_blocks: Any
process_nav: Any
process_nav_includes: Any
process_video_nav: Any
request: flask.wrappers.Request
resources: Callable
root_folder: str
set_replace_simple_code: Any
site_data: Dict[str, Any]
sys: module
threading: module
tutorial_img: Callable
url_adapter: Any
urls: Any
videos_page: Callable
walk_directory: Any
xmltodict: Any
yaml: module

AnyStr = TypeVar('AnyStr', str, bytes)

def generate_pdf(build_mode: bool, pages, toc) -> str: ...
def get_kotlin_features() -> list: ...
def get_nav() -> Any: ...
def get_nav_impl() -> Any: ...
def get_site_data() -> Dict[str, Any]: ...
def make_response(*args) -> Any: ...
def process_api_page(page_path) -> str: ...
def process_page(page_path) -> str: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def respond_with_package_list(page_path) -> Any: ...
def send_file(filename_or_fp, mimetype = ..., as_attachment: bool = ..., attachment_filename = ..., add_etags: bool = ..., cache_timeout = ..., conditional: bool = ..., last_modified = ...) -> Any: ...
def send_from_directory(directory, filename, **options) -> Any: ...
def url_for(endpoint, **values) -> Any: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
def validate_links_weak(page, page_path) -> None: ...
