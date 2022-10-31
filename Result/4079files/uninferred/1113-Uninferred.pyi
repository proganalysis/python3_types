from typing import Any, Optional

REDIS_LOCK_URL: Any
DEFAULT_PREFIX: Any
logger: Any

def get_redis_connection(): ...
def get_lock(resource: Any, expires: Any): ...
def acquires_lock(expires: Any, should_fail: bool = ..., should_wait: bool = ..., resource: Optional[Any] = ..., prefix: Any = ..., create_id: Optional[Any] = ...): ...