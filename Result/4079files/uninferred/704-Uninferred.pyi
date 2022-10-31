from typing import Any

class Config:
    FILE_PATH: str = ...
    DEFAULT_VALUE: Any = ...
    config: Any = ...
    value: Any = ...
    def __init__(self) -> None: ...
    def _save_config(self) -> None: ...
    def load_file_or_reset(self) -> None: ...
    def save_value(self) -> None: ...
    def _dict_to_config(self) -> None: ...
    def config_to_dict(self) -> None: ...

config: Any