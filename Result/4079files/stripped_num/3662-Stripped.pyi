# (generated with --quick)

import flask.app
import flask.wrappers
import jinja2.environment
from typing import Any, Callable, Tuple, Type

ExifTags: module
Flask: Type[flask.app.Flask]
Image: module
Template: Type[jinja2.environment.Template]
app: flask.app.Flask
base64: module
flask: module
index: Callable
keras: Any
load_model: Any
model: Any
np: module
os: module
predict: Callable
request: flask.wrappers.Request

def maybe_rotate(image) -> Any: ...
def predict_image(image) -> Tuple[Any, Any]: ...
