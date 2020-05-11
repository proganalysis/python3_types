# (generated with --quick)

from typing import Any, Optional

PluginScanCommand: Any
PluginScanResult: Any
ServerConnectivityInfo: Any
ServerConnectivityTester: Any
TlsWrappedProtocolEnum: Any

class MockCommandLineValues:
    def __init__(self) -> None: ...

class MockPluginScanCommandOne(Any):
    @classmethod
    def get_cli_argument(cls) -> str: ...
    @classmethod
    def get_title(cls) -> str: ...

class MockPluginScanCommandTwo(Any):
    @classmethod
    def get_cli_argument(cls) -> str: ...
    @classmethod
    def get_title(cls) -> str: ...

class MockPluginScanResult(Any):
    scan_command: Any
    text_output: Any
    xml_output: Any
    def __init__(self, server_info, scan_command, text_output, xml_output) -> None: ...
    def as_text(self) -> list: ...
    def as_xml(self) -> Any: ...

class MockServerConnectivityInfo(Any):
    client_auth_requirement: Any
    hostname: str
    http_tunneling_settings: Any
    ip_address: Optional[str]
    port: int
    tls_wrapped_protocol: Any
    def __init__(self, client_auth_requirement = ..., http_tunneling_settings = ...) -> None: ...

class MockServerConnectivityTester(Any):
    hostname: Any
    ip_address: str
    port: int
    tls_wrapped_protocol: Any
    def __init__(self, hostname = ...) -> None: ...
