# (generated with --quick)

import os
import redis.client
from typing import Any, Type, Union

Celery: Any
Redis: Type[redis.client.Redis]
app: Any
cache: redis.client.Redis
cache_database: Union[int, str]
cache_date_format: str
cache_ttl: Union[int, str]
celery_database: Union[int, str]
crontab: Any
environ: os._Environ[str]
get_task_logger: Any
logger: Any
redis_host: str
redis_port: Union[int, str]
refresh_hour: str
refresh_minute: Union[int, str]

def beat() -> None: ...
def housekeeping() -> None: ...
def worker() -> None: ...
