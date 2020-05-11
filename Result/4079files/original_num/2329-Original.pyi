# (generated with --quick)

import pathlib
from typing import Any, Coroutine, Type

BASE_DIR: pathlib.Path
EncryptedCookieStorage: Any
Path: Type[pathlib.Path]
Settings: Any
THIS_DIR: pathlib.Path
URL: Any
aiohttp_jinja2: Any
aiohttp_session: Any
base64: module
create_engine: Any
index: Any
jinja2: module
message_data: Any
messages: Any
web: Any

def cleanup(app) -> Coroutine[Any, Any, None]: ...
def create_app() -> coroutine: ...
def pg_dsn(settings) -> str: ...
def setup_routes(app) -> None: ...
def startup(app) -> Coroutine[Any, Any, None]: ...
