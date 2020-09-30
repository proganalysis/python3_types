# (generated with --quick)

import asyncio.locks
from typing import Any, Callable, Coroutine, Dict, Iterable, Optional, Type, TypeVar, Union

OnChangeType = Callable[[], None]
ValidatorsType = Iterable[Callable[[T], None]]

ChoiceCallableType: Type[Optional[Union[Callable[[], Optional[Iterable[Dict[str, str]]]], Iterable[Dict[str, str]]]]]
ChoiceType: Type[Optional[Iterable[Dict[str, str]]]]
ConfigError: Any
ConfigNotFound: Any
ConfigStore: Any
ConfigVariableDict: Any
DjangoValidationError: Any
INPUT_TYPE_MAPPING: Dict[str, Type[Union[dict, int, list, str]]]
TypedDict: Any
apps: Any
async_to_sync: Any
asyncio: module
build_key_to_id_lock: asyncio.locks.Lock
config: ConfigHandler
element_cache: Any

T = TypeVar('T')

class ConfigHandler:
    __doc__: str
    config_variables: dict
    key_to_id: Optional[dict]
    def __getitem__(self, key) -> Any: ...
    def __init__(self) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def async_get_key_to_id(self) -> coroutine: ...
    def build_key_to_id(self) -> Coroutine[Any, Any, None]: ...
    def cleanup_old_config_values(self) -> Any: ...
    def collect_config_variables_from_apps(self) -> None: ...
    def exists(self, key) -> bool: ...
    def get_collection_string(self) -> Any: ...
    def get_key_to_id(self) -> Any: ...
    def increment_version(self) -> None: ...
    def save_default_values(self) -> bool: ...
    def update_config_variables(self, items) -> None: ...

class ConfigVariable:
    __doc__: str
    choices: Any
    data: Any
    default_value: Any
    group: Any
    help_text: Any
    hidden: Any
    input_type: Any
    label: Any
    name: Any
    on_change: Any
    subgroup: Any
    validators: Any
    weight: Any
    def __init__(self, name, default_value, input_type = ..., label = ..., help_text = ..., choices = ..., hidden = ..., weight = ..., group = ..., subgroup = ..., validators = ..., on_change = ...) -> None: ...
    def is_hidden(self) -> Any: ...
