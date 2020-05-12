# (generated with --quick)

from typing import Any, Optional

Sanic: Any
create_redis_pool: Any

class SanicRedis:
    app: Any
    config: Optional[dict]
    conn: Any
    def __init__(self, app = ..., redis_config: Optional[dict] = ...) -> None: ...
    def init_app(self, app, redis_config: Optional[dict] = ...) -> None: ...
