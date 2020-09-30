# (generated with --quick)

from typing import Any, Coroutine, Optional

ClientError: Any
ClientSession: Any
ClientTimeout: Any
InAppPyValidationError: Any
api_result_errors: Any
api_result_ok: Any

class AppStoreValidator(Any):
    __doc__: str
    _session: Any
    sandbox: bool
    def __aenter__(self) -> Coroutine[Any, Any, None]: ...
    def __aexit__(self, exc_type, exc_val, exc_tb) -> Coroutine[Any, Any, None]: ...
    def __init__(self, bundle_id: str, sandbox: bool = ..., auto_retry_wrong_env_request: bool = ..., http_timeout: Optional[int] = ...) -> None: ...
    def post_json(self, request_json: dict) -> Coroutine[Any, Any, dict]: ...
    def validate(self, receipt: str, shared_secret: Optional[str] = ..., exclude_old_transactions: bool = ...) -> Coroutine[Any, Any, dict]: ...
