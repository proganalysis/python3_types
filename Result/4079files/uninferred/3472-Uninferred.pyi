from tornado import web as web
from typing import Any

logger: Any

def start_http(app: web.Application, http_port: int=..., usefork: bool=...) -> Any: ...
