# (generated with --quick)

from typing import Any, Callable, Dict, Type, Union

_NO_DEFAULT: Any
dataclasses: module
enum: module
os: module
transform_module: Any
warnings: module

class AutoConfig(Config):
    __doc__: str
    _options: Any
    def __init_subclass__(cls: AutoConfig, prefix = ..., **kwargs) -> None: ...

class Autoload(enum.Enum):
    CLASS: str
    NEVER: str
    OBJECT: str
    __doc__: str

class Config:
    __doc__: str
    _options: _Options
    def __init__(self, *args, **kwargs) -> None: ...
    def __init_subclass__(cls: Config, **kwargs) -> None: ...
    @classmethod
    def load(cls, target_obj = ...) -> None: ...

class Source(Dict[VariableName, VariableValue]):
    def __init__(self, val: Dict[VariableName, VariableValue]) -> None: ...

class TransformCallable(Callable[[VariableValue, type], Any]):
    def __init__(self, val: Callable[[VariableValue, type], Any]) -> None: ...

class Variable:
    __doc__: str
    default: Any
    source: Any
    transform: Any
    variable_name: Any
    wanted_type: Any
    def __init__(self) -> None: ...
    def get(self) -> Any: ...
    def set_defaults(self, *, variable_name, transform, source, wanted_type) -> None: ...

class VariableName(Union[bytes, str]):
    def __init__(self, val: Union[bytes, str]) -> None: ...

class VariableValue(Union[bytes, str]):
    def __init__(self, val: Union[bytes, str]) -> None: ...

class _Options:
    __doc__: str
    autoload: Any
    prefix: None
    source: os._Environ[str]
    transform: Any
    wanted_type: Type[str]
    def __init__(self) -> None: ...
    @classmethod
    def from_dict(cls, options_dict) -> Any: ...
    def variable_name(attr_name: _Options, prefix = ...) -> Any: ...

def _generate_environ_name(attr_name: _Options, prefix = ...) -> Any: ...
