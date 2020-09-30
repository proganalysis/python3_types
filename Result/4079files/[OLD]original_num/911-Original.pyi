# (generated with --quick)

import redis.client
from typing import Any, Dict

EVENT_FINISHED: Any
EventPerSecondAverage: Any
MovingAverage: Any
RedisHuey: Any
re: module
redis: module
threading: module

class EventQueue:
    average_execution_timings: Dict[Any, Dict[str, Any]]
    execution_stats: Any
    huey: Any
    name: Any
    prefix: str
    def __init__(self, name, connection_pool) -> None: ...
    def calculate_averages(self, name, event) -> None: ...
    def clean_event_name(self, name) -> Any: ...
    def listen(self) -> None: ...

class TaskQueue:
    average: Any
    clean_name: Any
    event_queue: EventQueue
    growing_threshold: int
    length: Any
    name: Any
    redis_connection: redis.client.Redis
    redis_queue: str
    redis_schedule: str
    scheduled: Any
    def __init__(self, name, connection_pool) -> None: ...
    def is_growing(self) -> Any: ...
    def is_shrinking(self) -> Any: ...
    def update(self) -> None: ...
