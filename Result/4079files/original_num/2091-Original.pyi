# (generated with --quick)

import flask.app
import flask.wrappers
import io
from typing import Any, Callable, List, Optional, Type

Flask: Type[flask.app.Flask]
Node: Any
PGM: Any
Response: Type[flask.wrappers.Response]
StringIO: Type[io.StringIO]
app: flask.app.Flask
math: module
render: Callable
request: flask.wrappers.Request
static_file: Callable
uuid: module

class GraphGenerationHelpers:
    def add_label(self, graph, text: str, x: float, y: float, label_id: Optional[str] = ..., color: Optional[str] = ..., size: Optional[str] = ..., weight: Optional[str] = ...) -> None: ...
    def add_label_range(self, graph, labels: List[str], x: float, y: float, spacing: float = ..., spacing_exp: float = ..., direction: str = ..., overrides: Optional[dict] = ..., **other_label_args) -> None: ...
    def fully_connect(self, graph, layer1: list, layer2: list) -> None: ...
    def layer(self, graph, node_texts: List[str], x: float, y: float, spacing: float = ..., spacing_pow: float = ..., **other_node_params) -> list: ...

def send_from_directory(directory, filename, **options) -> Any: ...
def unquote(string: str, encoding: str = ..., errors: str = ...) -> str: ...
