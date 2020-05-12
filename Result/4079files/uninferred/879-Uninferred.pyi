from typing import Any, Optional
from werkzeug.routing import BaseConverter

SECRET: Any
PASSWORD: Any
JWT_SECRET: Any
PROJECTS: Any

class StringConverter(BaseConverter):
    exc: Any = ...
    def __init__(self, url_map: Any, exc: str = ...) -> None: ...
    def to_python(self, value: Any): ...
    def to_url(self, value: Any): ...

app: Any
channel: Any

def check_auth(func: Any): ...
def error_handler(func: Any): ...
def nocache(view: Any): ...
def SSEPing() -> None: ...
def login(): ...
def list_projects(): ...
def get_builds(proj: Any): ...
def get_build_details(proj: Any, ref: Any): ...
def get_diff(proj: Any, ref: Any, ref2: Any): ...
def subscribe(): ...

useNginx: Any

def mySendFile(path: Any, mimetype: Any, content_disposition: Optional[Any] = ...): ...
def get_build_log(proj: Any, ref: Any): ...
def get_build_svg(proj: Any, ref: Any): ...
def get_build_pdf(proj: Any, ref: Any): ...
def get_build_zip(proj: Any, ref: Any): ...
def get_latest_svg(proj: Any): ...
def start_build(proj: Any, ref: Any): ...
def github_build(proj: Any): ...
