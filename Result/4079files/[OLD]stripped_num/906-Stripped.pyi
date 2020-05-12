# (generated with --quick)

from typing import Any

Serializer: Any
check_argument_types: Any
yaml: Any

class YAMLSerializer(Any):
    __slots__ = ["_dumper_class", "_dumper_options", "_loader_class"]
    __doc__: str
    _dumper_class: Any
    _dumper_options: Any
    _loader_class: Any
    mimetype: str
    safe: bool
    def __init__(self, safe = ..., dumper_options = ...) -> None: ...
    def deserialize(self, payload) -> Any: ...
    def serialize(self, obj) -> Any: ...
