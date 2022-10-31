from typing import Any, Optional

class Config:
    path_to_config: Any = ...
    config: Any = ...
    def __init__(self, config_file: Optional[Any] = ...) -> None: ...
    def __getattr__(self, name: Any): ...
    @staticmethod
    def get_config_path(config_file: Any): ...
    def get_config(self): ...
    def merge(self, cli: Any) -> None: ...