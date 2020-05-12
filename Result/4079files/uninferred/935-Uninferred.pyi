from typing import Any

class ApiResource:
    raw: Any = ...
    def __init__(self, raw: Any) -> None: ...
    @property
    def id(self): ...
    @property
    def name(self): ...
    @property
    def created_at(self): ...
    @property
    def path(self) -> None: ...
    def observe(self, callback: Any, err_callback: Any, duration: int = ...): ...
    def set_name(self, name: Any): ...
    def set_values(self, values: Any): ...
    def update(self): ...
