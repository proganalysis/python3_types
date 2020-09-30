# (generated with --quick)

from typing import Any, Callable, Optional, Tuple, Type

CertRetrieveFunc = Callable[[int], str]
ValidateFunc = Callable[[int], Tuple[CertificateStatus, Optional[datetime.datetime]]]

Bottle: Any
HTTPResponse: Any
OCSPRequest: Any
OCSPResponse: Any
OCSPResponseBuilder: Any
asymmetric: Any
base64: module
datetime: Type[datetime.datetime]
enum: module
logger: logging.Logger
logging: module
request: Any
timedelta: Type[datetime.timedelta]
timezone: Type[datetime.timezone]

class CertificateStatus(enum.Enum):
    affiliation_changed: str
    ca_compromise: str
    certificate_hold: str
    cessation_of_operation: str
    good: str
    key_compromise: str
    privilege_withdrawn: str
    remove_from_crl: str
    revoked: str
    superseded: str
    unknown: str

class OCSPResponder:
    _app: Any
    _cert_retrieve: Callable[[int], str]
    _issuer_cert: Any
    _next_update_days: int
    _responder_cert: Any
    _responder_key: Any
    _validate: Callable[[int], Tuple[CertificateStatus, Optional[datetime.datetime]]]
    def __init__(self, issuer_cert: str, responder_cert: str, responder_key: str, validate_func: Callable[[int], Tuple[CertificateStatus, Optional[datetime.datetime]]], cert_retrieve_func: Callable[[int], str], next_update_days: int = ...) -> None: ...
    def _build_http_response(self, request_der: bytes) -> Any: ...
    def _build_ocsp_response(self, ocsp_request) -> Any: ...
    def _fail(self, status: ResponseStatus) -> Any: ...
    def _handle_get(self, request_data) -> Any: ...
    def _handle_post(self) -> Any: ...
    def _handle_root(self) -> str: ...
    def _parse_ocsp_request(self, request_der: bytes) -> Any: ...
    def _route(self) -> None: ...
    def serve(self, port = ..., debug = ...) -> None: ...

class ResponseStatus(enum.Enum):
    internal_error: str
    malformed_request: str
    sign_required: str
    successful: str
    try_later: str
    unauthorized: str
