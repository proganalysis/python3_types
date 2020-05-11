# (generated with --quick)

from typing import Any, Dict, Optional

Serializer: Any
check_argument_types: Any
yaml: Any

class YAMLSerializer(Any):
    __slots__ = ["_dumper_class", "_dumper_options", "_loader_class"]
    __doc__: str
    _dumper_class: Any
    _dumper_options: Dict[str, Any]
    _loader_class: Any
    mimetype: str
    safe: bool
    def __init__(self, safe: bool = ..., dumper_options: Optional[Dict[str, Any]] = ...) -> None: ...
    def deserialize(self, payload: bytes) -> Any: ...
    def serialize(self, obj) -> bytes: ...
