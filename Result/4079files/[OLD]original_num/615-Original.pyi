# (generated with --quick)

from typing import Any

BaseDecoder: Any
BaseEncoder: Any
DecodingError: Any
EncodingError: Any
NULL_ENCODING: bytes
decode_single: Any
encode_single: Any
registry: Any

class DecodeNull(Any):
    word_width: None
    def decode(self, stream) -> None: ...
    @classmethod
    def from_type_str(cls, type_str, registry) -> Any: ...

class EncodeNull(Any):
    word_width: None
    def encode(self, value) -> bytes: ...
    @classmethod
    def from_type_str(cls, type_str, registry) -> Any: ...
    def validate_value(self, value) -> None: ...

def decode_null(stream) -> None: ...
def encode_null(x) -> bytes: ...
def test_register_and_use_callables() -> None: ...
def test_register_and_use_coder_classes() -> None: ...
