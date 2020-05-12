# (generated with --quick)

import __future__
from typing import Any

TSocketOverHttpTunnel: Any
TTransportException: Any
absolute_import: __future__._Feature
division: __future__._Feature
print_function: __future__._Feature
socket: module
ssl: module
unicode_literals: __future__._Feature

class TSSLSocketOverHttpTunnel(Any):
    ca_certs: Any
    cert_reqs: Any
    certfile: Any
    handle: ssl.SSLSocket
    keyfile: Any
    ssl_version: Any
    def __init__(self, host, port, proxy_host, proxy_port, ssl_version = ..., cert_reqs = ..., ca_certs = ..., keyfile = ..., certfile = ...) -> None: ...
    def open(self) -> None: ...
