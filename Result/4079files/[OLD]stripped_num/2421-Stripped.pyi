# (generated with --quick)

from typing import Any, Coroutine

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
    def __init__(self, bundle_id, sandbox = ..., auto_retry_wrong_env_request = ..., http_timeout = ...) -> None: ...
    def post_json(self, request_json) -> coroutine: ...
    def validate(self, receipt, shared_secret = ..., exclude_old_transactions = ...) -> coroutine: ...
