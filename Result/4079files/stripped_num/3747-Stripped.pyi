# (generated with --quick)

from typing import Any, TypeVar

JsonResponse: Any
json: module
serializers: Any

_T0 = TypeVar('_T0')

class GameSerializer(Any):
    name: Any
    settings: Any
    status: Any
    def get_settings_as_dict(self, game) -> str: ...
    def update(self, instance: _T0, validated_data) -> _T0: ...
