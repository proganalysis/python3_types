# (generated with --quick)

import os
from typing import Any

Applications: Any
CurrentUser: Any
Friends: Any
Groups: Any
Overlay: Any
Screenshots: Any
SteamApiStartupError: Any
Utils: Any
_ApiResourceBase: Any
_set_client: Any
environ: os._Environ[str]

class Api(Any):
    __doc__: str
    _app_id: Any
    _client: None
    _lib: Any
    app_id: Any
    apps: Any
    current_user: Any
    friends: Any
    groups: Any
    install_path: Any
    overlay: Any
    screenshots: Any
    steam_running: Any
    utils: Any
    def __init__(self, library_path, app_id = ...) -> None: ...
    def init(self, app_id = ...) -> None: ...
    def run_callbacks(self) -> None: ...
    @classmethod
    def set_app_id(cls, app_id) -> None: ...
    def shutdown(self) -> None: ...
    def start_app(self) -> Any: ...
