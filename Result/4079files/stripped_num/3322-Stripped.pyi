# (generated with --quick)

from typing import Any

logging: module
math: module
requests: module

class Harvester:
    _base_url: str
    _batch_size: int
    _processed_batches_counter: int
    logger: logging.Logger
    polygons: Any
    def __init__(self, include_polygons = ...) -> None: ...
    def _get_batch(self, scroll_id) -> Any: ...
    def _handle_query_exception(self, e, retries_left) -> Any: ...
    def _retry_query(self, url, retries_left) -> Any: ...
    def get_data(self) -> Any: ...
