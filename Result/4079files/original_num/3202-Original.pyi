# (generated with --quick)

import html.parser
import pyVK.exceptions
from typing import Any, Type

HTMLParser: Type[html.parser.HTMLParser]
VKAuthError: Type[pyVK.exceptions.VKAuthError]
cookiejar: module
error: module
json: module
parse: module
re: module
request: module

class Api:
    expires_in: Any
    token: Any
    user_id: Any
    v_api: Any
    def __init__(self, v_api, token = ..., expires_in = ..., user_id = ...) -> None: ...
    def auth(self, app_id, scope, login, password) -> None: ...
    def call_method(self, method: str, params: dict) -> Any: ...

class AuthFormParser(html.parser.HTMLParser):
    _form_parsed: bool
    _in_form: bool
    method: Any
    params: dict
    url: Any
    def __init__(self) -> None: ...
    def error(self, message) -> None: ...
    def handle_endtag(self, tag) -> None: ...
    def handle_starttag(self, tag, attrs) -> None: ...
