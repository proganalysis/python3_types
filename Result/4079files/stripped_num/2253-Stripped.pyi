# (generated with --quick)

from typing import Any, Dict

ModelSerializer: Any
pluralize: Any
post_dump: Any
pre_load: Any

class WrappedSerializer(Any):
    __doc__: str
    __envelop__: Dict[str, None]
    unwrap_envelope: Any
    wrap_with_envelope: Any
    def get_envelope_key(self, many) -> Any: ...
