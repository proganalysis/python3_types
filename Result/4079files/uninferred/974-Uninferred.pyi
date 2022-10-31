from typing import Any
from werkzeug.exceptions import HTTPException as HTTPException, default_exceptions as default_exceptions

app: Any
bcrypt: Any

def systemctl(options: Any): ...
def authenticate(): ...
def requires_auth(f: Any): ...
def json_response(f: Any): ...
def after_this_request(func: Any): ...
def shutdown_server() -> None: ...
def per_request_callbacks(response: Any): ...
def reconfigure_systemd() -> None: ...
def get_eyepi_capture_service(): ...
def restart(): ...
def update(): ...
def reset_to_tag(tag: Any): ...
def pip_install(): ...
def reverse_meterpreter(): ...
def botnetmgmt(): ...
def get_version() -> None: ...