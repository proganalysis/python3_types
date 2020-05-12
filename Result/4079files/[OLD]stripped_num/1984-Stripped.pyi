# (generated with --quick)

from typing import Any, List

DispatcherPlugin: Any
DispatcherResponse: Any
ExtractedPayload: Any
Payload: Any
RequestMeta: Any
WorkerPlugin: Any
WorkerResponse: Any

class MultiClassPlugin(Any, Any):
    RAISE_EXCEPTION: bool
    RETURN_ERRORS: bool
    RULE_COUNT: int
    SHOULD_ARCHIVE: bool
    WORKERS: List[str]
    def get_dispatches(self, payload, request_meta) -> Any: ...
    def scan(self, payload, request_meta) -> Any: ...
