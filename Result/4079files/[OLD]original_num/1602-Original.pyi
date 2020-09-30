# (generated with --quick)

from typing import Any, Callable, Dict, Optional, Union

_NO_DEFAULT: Any
dataclasses: module
enum: module
os: module
transform_module: Any
warnings: module

class AutoConfig(Config):
    __doc__: str
    _options: Any
    def __init_subclass__(cls: AutoConfig, prefix: Optional[str] = ..., **kwargs) -> None: ...

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
    def load(cls: Config, target_obj: object = ...) -> None: ...

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
    def __init__(self, variable_name: Optional[VariableName] = ..., default = ..., transform: Optional[TransformCallable] = ..., source: Optional[Source] = ...) -> None: ...
    def get(self) -> VariableValue: ...
    def set_defaults(self, *, variable_name: VariableName, transform: TransformCallable, source: Source, wanted_type: type) -> None: ...

class VariableName(Union[bytes, str]):
    def __init__(self, val: Union[bytes, str]) -> None: ...

class VariableValue(Union[bytes, str]):
    def __init__(self, val: Union[bytes, str]) -> None: ...

class _Options:
    __doc__: str
    autoload: Autoload
    prefix: Optional[str]
    source: Source
    transform: TransformCallable
    variable_name: Callable[[str, Optional[str]], VariableName]
    wanted_type: Any
    def __init__(self, prefix: Optional[str] = ..., autoload: Autoload = ..., source: Source = ..., transform: TransformCallable = ..., wanted_type = ..., variable_name: Callable[[str, Optional[str]], VariableName] = ...) -> None: ...
    @classmethod
    def from_dict(cls, options_dict: dict) -> _Options: ...

def _generate_environ_name(attr_name: str, prefix: Optional[str] = ...) -> VariableName: ...
