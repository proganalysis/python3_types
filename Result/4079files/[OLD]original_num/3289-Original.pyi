# (generated with --quick)

import flask.app
from typing import Any

_: Any
bootstrap: Any
click: module
combine_navigation_entries: functools._lru_cache_wrapper
config: module
copy: module
exceptions: module
flask: module
functools: module
layout: module
navigation: Any
response: Any
sys: module
types: module
typing: module

class MaraApp(flask.app.Flask):
    def __init__(self) -> None: ...
    def disable_caching(self) -> None: ...
    def patch_flask_url_for(self) -> None: ...
    def register_blueprints(self) -> None: ...
    def register_commands(self) -> None: ...
    def register_error_handlers(self) -> None: ...
    def register_page_layout(self) -> None: ...

def module_functionalities(module: module, MARA_XXX: str, type) -> Any: ...
