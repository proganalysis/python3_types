# (generated with --quick)

import enum
from typing import Any, Callable, Dict, List, Tuple, Type, Union

CollapsibleBase: Any
EXCEPTION_MESSAGE: Any
Enum: Type[enum.Enum]
RDOperator: Any
bpy: Any
core_logger: Any
inspect: module
log_callstack: Any
os: module
resource_path: Any

class PluginManager(object):
    PluginTypes: enum.Enum
    __doc__: str
    _bl_icons_dict: None
    _bools_to_register: list
    _classes_to_register: List[Tuple[Any, Union[tuple, List[nothing]]]]
    _file_plugins: List[nothing]
    _icons_to_register: List[nothing]
    _property_fields: Dict[nothing, nothing]
    _property_groups_to_register: List[Tuple[Any, Any]]
    _registered_bools: List[nothing]
    _registered_classes: List[nothing]
    _registered_properties: List[nothing]
    @classmethod
    def clear(cls) -> None: ...
    @classmethod
    def getFilePlugins(cls, type_ = ...) -> Any: ...
    @classmethod
    def get_icon(cls, id: str) -> Any: ...
    @classmethod
    def get_property(cls, obj, prop) -> None: ...
    @classmethod
    def load_icon(cls, id: str, filename: str) -> None: ...
    @classmethod
    def register(cls) -> None: ...
    @staticmethod
    def register_class(*args) -> Any: ...
    @classmethod
    def register_collapsible(cls, property_name) -> None: ...
    @classmethod
    def register_plugin(cls, label, operators, draw_function = ..., type_ = ...) -> None: ...
    @staticmethod
    def register_property_group(base = ...) -> Callable[[Any], Any]: ...
    @classmethod
    def register_property_groups(cls, property_group, btype) -> None: ...
    @classmethod
    def unregister(cls) -> None: ...
