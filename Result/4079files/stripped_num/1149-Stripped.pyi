# (generated with --quick)

from typing import Any, Callable, Tuple

CustomizableSerializer: Any
DefaultCustomTypeCodec: Any
ExtType: Any
check_argument_types: Any
packb: Any
resolve_reference: Any
unpackb: Any

class MsgpackSerializer(Any):
    __slots__ = ["_marshallers", "_unmarshallers", "custom_type_codec", "packer_options", "unpacker_options"]
    __doc__: str
    mimetype: str
    packer_options: Any
    unpacker_options: Any
    def __init__(self, packer_options = ..., unpacker_options = ..., custom_type_codec = ...) -> None: ...
    def deserialize(self, payload) -> Any: ...
    def serialize(self, obj) -> Any: ...

class MsgpackTypeCodec(Any):
    __doc__: str
    serializer: Any
    type_code: Any
    unwrap_callback: Callable[[Any], Any]
    wrap_callback: Callable[[Any, Any], Any]
    def __init__(self, type_code = ..., **kwargs) -> None: ...
    def ext_hook(self, code, data) -> Any: ...
    def register_object_decoder_hook(self, serializer) -> None: ...
    def register_object_encoder_hook(self, serializer) -> None: ...
    def unwrap_state_ext_type(self, wrapped_state) -> Tuple[Any, Any]: ...
    def wrap_state_ext_type(self, typename, state) -> Any: ...
