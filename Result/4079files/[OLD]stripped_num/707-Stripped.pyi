# (generated with --quick)

import pathlib
from typing import Any, Type

CURRENT_PLATFORM: Any
ClientAuthConfigEnum: Any
ClientCertificateRequested: Any
CouldNotBuildVerifiedChain: Any
LegacyOpenSslServer: Any
LegacySslClient: Any
ModernOpenSslServer: Any
OpenSSLError: Any
OpenSslEarlyDataStatusEnum: Any
OpenSslVerifyEnum: Any
OpenSslVersionEnum: Any
Path: Type[pathlib.Path]
SslClient: Any
SupportedPlatformEnum: Any
TestModernSslClientOnlineTls13: Any
TestSslClientClientAuthentication: Any
TestSslClientOnline: Any
_nassl: Any
pytest: Any
socket: module

class TestLegacySslClientOnlineSsl2:
    def test_ssl_2(self) -> None: ...

class TestModernSslClientOnline:
    def test_get_verified_chain(self) -> None: ...
    def test_get_verified_chain_but_validation_failed(self) -> None: ...
