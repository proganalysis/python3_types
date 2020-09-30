# (generated with --quick)

import collections
from typing import Any, Type

CERTS_TOTAL: Any
CERT_DIR: Any
CertificateChain: Any
Gauge: Any
TRC: Any
TRCS_TOTAL: Any
defaultdict: Type[collections.defaultdict]
glob: module
logging: module
os: module
read_file: Any
threading: module
write_file: Any

class TrustStore(object):
    __doc__: str
    _cachedir: Any
    _certs: collections.defaultdict
    _certs_lock: threading.Lock
    _dir: Any
    _ename: Any
    _labels: Any
    _trcs: collections.defaultdict
    _trcs_lock: threading.Lock
    def __init__(self, conf_dir, cache_dir, ename, labels = ...) -> None: ...
    def _init_certs(self) -> None: ...
    def _init_metrics(self) -> None: ...
    def _init_trcs(self) -> None: ...
    def add_cert(self, cert, write = ...) -> None: ...
    def add_trc(self, trc, write = ...) -> None: ...
    def get_cert(self, isd_as, version = ...) -> Any: ...
    def get_trc(self, isd, version = ...) -> Any: ...
    def get_trcs(self) -> list: ...
