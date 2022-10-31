from .base import TimeSeriesBase
from typing import Any

class MongoTimeSeries(TimeSeriesBase):
    server: Any = ...
    resolution: Any = ...
    _db: Any = ...
    client: Any = ...
    def __init__(self, resolution: Any, db: str = ..., server: str = ...) -> None: ...
    @property
    def db(self): ...
    def get_collection(self) -> None: ...
    def ensure_index(self) -> None: ...
    def add_many(self, key: Any, data: Any, *args: Any, **kwargs: Any) -> None: ...
    def get(self, *args: Any, **kwargs: Any) -> None: ...
    def add(self, name: Any, *args: Any, **kwargs: Any) -> None: ...
    @property
    def query(self) -> None: ...
    def _set_index(self) -> None: ...

class MongoTickStore(TimeSeriesBase): ...