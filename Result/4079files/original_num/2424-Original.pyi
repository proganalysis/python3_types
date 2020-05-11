# (generated with --quick)

import flask.app
import io
import subprocess
from typing import Any, Callable, Dict, Iterable, Set, Type, Union

DEFAULT_LANG: str
Flask: Type[flask.app.Flask]
PIPE: int
Popen: Type[subprocess.Popen]
QqParser: Any
QqTag: Any
STDOUT: int
StringIO: Type[io.StringIO]
allowed_tags: Set[str]
app: flask.app.Flask
contextlib: module
itertools: module
mistune: Any
os: module
show: Callable
show_default: Callable
show_filename: Callable
stdout_io: Callable[..., contextlib._GeneratorContextManager]
sys: module
translations: Dict[str, str]

def node_exec(code) -> str: ...
def process_js(tag) -> Any: ...
def process_prlang(tag, prlang) -> Any: ...
def process_python(tag) -> Any: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def strip_blank_lines(code) -> str: ...
