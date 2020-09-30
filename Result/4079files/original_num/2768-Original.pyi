# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, Callable, Dict, Iterable, List, Type, Union

Flask: Type[flask.app.Flask]
app: flask.app.Flask
domain: str
file: Any
files: List[Dict[str, Any]]
get_annotations: Callable
get_document: Callable
get_documents: Callable
glob: module
gold_info: Any
grouped_documents: List[Dict[str, Union[str, List[Dict[str, Any]]]]]
id: int
index: Callable
json: module
lang: str
os: module
path: module
request: flask.wrappers.Request
send_css: Callable
send_js: Callable

def __getattr__(name) -> Any: ...
def get_mention_by_startindex_for_document(mentions_df, doc: str) -> Dict[int, list]: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def send_from_directory(directory, filename, **options) -> Any: ...
