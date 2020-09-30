from typing import Any

logger: Any
redis_host: Any
redis_port: Any
cache_ttl: Any
cache_database: Any
celery_database: Any
refresh_minute: Any
refresh_hour: Any
cache: Any
cache_date_format: str
app: Any

def beat() -> None: ...
def housekeeping() -> None: ...
def worker() -> None: ...
