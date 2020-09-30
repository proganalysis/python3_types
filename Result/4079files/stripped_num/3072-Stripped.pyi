# (generated with --quick)

from typing import Any

Sanic: Any
create_redis_pool: Any

class SanicRedis:
    app: Any
    config: Any
    conn: Any
    def __init__(self, app = ..., redis_config = ...) -> None: ...
    def init_app(self, app, redis_config = ...) -> None: ...
