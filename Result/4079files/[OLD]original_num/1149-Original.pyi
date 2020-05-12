# (generated with --quick)

from typing import Any, Callable, Dict, Optional, Tuple, Union

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
    def __init__(self, packer_options: Optional[Dict[str, Any]] = ..., unpacker_options: Optional[Dict[str, Any]] = ..., custom_type_codec: Optional[Union[MsgpackTypeCodec, str]] = ...) -> None: ...
    def deserialize(self, payload: bytes) -> Any: ...
    def serialize(self, obj) -> bytes: ...

class MsgpackTypeCodec(Any):
    __doc__: str
    serializer: MsgpackSerializer
    type_code: Any
    unwrap_callback: Callable[[bytes], Tuple[Optional[str], Any]]
    wrap_callback: Callable[[str, Any], Any]
    def __init__(self, type_code: Optional[int] = ..., **kwargs) -> None: ...
    def ext_hook(self, code: int, data: bytes) -> Any: ...
    def register_object_decoder_hook(self, serializer: MsgpackSerializer) -> None: ...
    def register_object_encoder_hook(self, serializer: MsgpackSerializer) -> None: ...
    def unwrap_state_ext_type(self, wrapped_state: bytes) -> Tuple[Optional[str], Any]: ...
    def wrap_state_ext_type(self, typename: str, state) -> Any: ...
