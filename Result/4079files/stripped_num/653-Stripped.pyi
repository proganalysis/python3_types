# (generated with --quick)

import threading
from typing import Any, Type

ObjectValidationFailedException: Any
Output: Any
Thread: Type[threading.Thread]
get_entity_type_from_object: Any

class ValidationWorker(threading.Thread):
    check_pool: Any
    current_object: Any
    id: Any
    queue: Any
    result: Any
    seen_list: Any
    def __init__(self, id, queue, seen_list, check_pool, result) -> None: ...
    def is_seen_object(self) -> bool: ...
    def save_failed_object(self) -> None: ...
    def save_validation_results(self, validation_results) -> None: ...
    def validate_object(self) -> Any: ...

def sleep(secs: float) -> None: ...
