# (generated with --quick)

import json.encoder
from typing import Any, Callable, Optional, Tuple, Type, Union

text: Any

def json_dumps(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
def skip_test_utf8_route(app) -> None: ...
def test_utf8_post_json(app) -> None: ...
def test_utf8_query_string(app) -> None: ...
def test_utf8_response(app) -> None: ...
