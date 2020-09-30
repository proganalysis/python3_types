# (generated with --quick)

import flask.app
import flask.wrappers
import io
from typing import Any, Callable, Type

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
    def add_label(self, graph, text, x, y, label_id = ..., color = ..., size = ..., weight = ...) -> None: ...
    def add_label_range(self, graph, labels, x, y, spacing = ..., spacing_exp = ..., direction = ..., overrides = ..., **other_label_args) -> None: ...
    def fully_connect(self, graph, layer1, layer2) -> None: ...
    def layer(self, graph, node_texts, x, y, spacing = ..., spacing_pow = ..., **other_node_params) -> list: ...

def send_from_directory(directory, filename, **options) -> Any: ...
def unquote(string: str, encoding: str = ..., errors: str = ...) -> str: ...
