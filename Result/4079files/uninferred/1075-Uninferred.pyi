import lightbus
from lightbus.serializers import MessageDeserializer, MessageSerializer
from typing import Any

class ByFieldMessageSerializer(MessageSerializer):
    def __call__(self, message: lightbus.Message) -> dict: ...

class ByFieldMessageDeserializer(MessageDeserializer):
    def __call__(self, serialized: dict, *, native_id: Any=..., **extra: Any) -> Any: ...
