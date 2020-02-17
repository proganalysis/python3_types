# (generated with --quick)

from typing import Any

MessageDeserializer: Any
MessageSerializer: Any
decode_bytes: Any
lightbus: Any
sanity_check_metadata: Any

class ByFieldMessageDeserializer(Any):
    def __call__(self, serialized: dict, *, native_id = ..., **extra) -> Any: ...

class ByFieldMessageSerializer(Any):
    def __call__(self, message) -> dict: ...
