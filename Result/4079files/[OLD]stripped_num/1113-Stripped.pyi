# (generated with --quick)

import datetime
import redis.client
from typing import Any, Callable, Sequence, Type

DEFAULT_PREFIX: Any
ImproperlyConfigured: Any
REDIS_LOCK_URL: Any
StrictRedis: Type[redis.client.Redis]
logger: logging.Logger
logging: module
redis_lock: Any
settings: Any
timedelta: Type[datetime.timedelta]

def acquires_lock(expires, should_fail = ..., should_wait = ..., resource = ..., prefix = ..., create_id = ...) -> Callable[[Any], Any]: ...
def get_lock(resource, expires) -> Any: ...
def get_redis_connection() -> redis.client.Redis: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
