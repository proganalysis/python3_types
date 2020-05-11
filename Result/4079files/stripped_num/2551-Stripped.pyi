# (generated with --quick)

from typing import Any, Callable

BaseSslClient: Any
ClientCertificateRequested: Any
OpenSslFileTypeEnum: Any
OpenSslVerifyEnum: Any
OpenSslVersionEnum: Any
WantReadError: Any
WantX509LookupError: Any
_nassl_legacy: Any
socket: module
sys: module

class LegacySslClient(Any):
    _NASSL_MODULE: Any
    _SSL_MODE_SEND_FALLBACK_SCSV: int
    __doc__: str
    _is_handshake_completed: bool
    do_handshake: Callable[[], Any]
    def __init__(self, underlying_socket = ..., ssl_version = ..., ssl_verify = ..., ssl_verify_locations = ..., client_certchain_file = ..., client_key_file = ..., client_key_type = ..., client_key_password = ..., ignore_client_authentication_requests = ...) -> None: ...
    def do_renegotiate(self) -> None: ...
    def do_ssl2_iis_handshake(self) -> None: ...
    def enable_fallback_scsv(self) -> None: ...
    @staticmethod
    def get_available_compression_methods() -> Any: ...
    def get_current_compression_method(self) -> Any: ...
    def get_secure_renegotiation_support(self) -> Any: ...
