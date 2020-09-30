from tornado import web
from typing import Any

logger: Any

class MainHandler(web.RequestHandler):
    def get(self) -> None: ...
