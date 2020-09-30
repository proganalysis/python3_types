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
    bundle_id: str
    public_key: Any
    purchase_state_ok: int
    def __init__(self, bundle_id: str, api_key: str, default_valid_purchase_state: int = ...) -> None: ...
    def _validate_signature(self, receipt: str, signature: str) -> bool: ...
    def validate(self, receipt: str, signature: str) -> dict: ...

class GooglePlayVerifier:
    bundle_id: str
    http: Any
    http_timeout: int
    private_key_path: str
    def __init__(self, bundle_id: str, private_key_path: str, http_timeout: int = ...) -> None: ...
    def _authorize(self) -> Any: ...
    @staticmethod
    def _ms_timestamp_expired(ms_timestamp: str) -> bool: ...
    def check_purchase_product(self, purchase_token: str, product_sku: str, service) -> dict: ...
    def check_purchase_subscription(self, purchase_token: str, product_sku: str, service) -> dict: ...
    def verify(self, purchase_token: str, product_sku: str, is_subscription: bool = ...) -> dict: ...
    def verify_with_result(self, purchase_token: str, product_sku: str, is_subscription: bool = ...) -> GoogleVerificationResult: ...

class GoogleVerificationResult:
    __doc__: str
    is_canceled: bool
    is_expired: bool
    raw_response: dict
    def __init__(self, raw_response: dict, is_expired: bool, is_canceled: bool) -> None: ...
    def __repr__(self) -> str: ...

def make_pem(public_key: str) -> str: ...
