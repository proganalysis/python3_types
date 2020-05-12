# (generated with --quick)

from typing import Any

SentryHandler: Any
logger: Any
logging: module
raven: Any
raven_aiohttp: Any
sanic: Any

class SanicSentry:
    app: Any
    client: Any
    handler: Any
    def __init__(self, app = ...) -> None: ...
    def init_app(self, app) -> None: ...
