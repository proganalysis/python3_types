# (generated with --quick)

from typing import Any

GoogleError: Any
HttpError: Any
InAppPyValidationError: Any
ServiceAccountCredentials: Any
base64: module
build: Any
datetime: module
httplib2: module
json: module
rsa: Any

class GooglePlayValidator:
    bundle_id: Any
    public_key: Any
    purchase_state_ok: Any
    def __init__(self, bundle_id, api_key, default_valid_purchase_state = ...) -> None: ...
    def _validate_signature(self, receipt, signature) -> Any: ...
    def validate(self, receipt, signature) -> Any: ...

class GooglePlayVerifier:
    bundle_id: Any
    http: Any
    http_timeout: Any
    private_key_path: Any
    def __init__(self, bundle_id, private_key_path, http_timeout = ...) -> None: ...
    def _authorize(self) -> Any: ...
    @staticmethod
    def _ms_timestamp_expired(ms_timestamp) -> bool: ...
    def check_purchase_product(self, purchase_token, product_sku, service) -> Any: ...
    def check_purchase_subscription(self, purchase_token, product_sku, service) -> Any: ...
    def verify(self, purchase_token, product_sku, is_subscription = ...) -> Any: ...
    def verify_with_result(self, purchase_token, product_sku, is_subscription = ...) -> GoogleVerificationResult: ...

class GoogleVerificationResult:
    __doc__: str
    is_canceled: Any
    is_expired: Any
    raw_response: Any
    def __init__(self, raw_response, is_expired, is_canceled) -> None: ...
    def __repr__(self) -> str: ...

def make_pem(public_key) -> str: ...
